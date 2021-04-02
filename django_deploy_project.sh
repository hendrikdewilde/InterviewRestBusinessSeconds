#!/bin/bash
#
# Usage: django_deploy_project.sh 3 mydomain.co.za /home/ubuntu/InterviewRestBusinessSeconds/
#

PYTHON_VER=$1
DOMAIN=$2
CURRENT_APP_PATH=$3

# Check if arguments was supplied
if [ "$PYTHON_VER" == "" ] || [ "$DOMAIN" == "" ] || [ "$CURRENT_APP_PATH" == "" ]; then
	echo "Usage:"
	echo "  $ django_deploy_project.sh <python-version> <domain-name> <current-app-path>"
	echo
	echo "  Python version, Domain name and Current App Path not specified."
	exit 1
fi

# Check if user is root
if [ "$EUID" -ne 0 ]; then
    echo "Must be root."
    exit 1
fi

# Check if python version is 3
if [ "$PYTHON_VER" != "3" ]; then
    echo "Invalid Python version."
    exit 1
fi

# Install Packages
LINUX_REQ=('git' 'build-essential' 'python3-dev' 'python3-pip' 'nginx' 'rsync' )
echo "Checking if installed."
declare -a MISSING
for pkg in "${LINUX_REQ[@]}"
    do
        echo "Installing '$pkg'..."
        apt-get -y install $pkg
        if [ $? -ne 0 ]; then
            echo "Error installing package '$pkg'"
            exit 1
        fi
    done

PYTHON_REQ=('virtualenv' 'supervisor')
for ppkg in "${PYTHON_REQ[@]}"
    do
        echo "Installing Python package '$ppkg'..."
        pip3 install $ppkg
        if [ $? -ne 0 ]; then
            echo "Error installing python package '$ppkg'"
            exit 1
        fi
    done

if [ ${#MISSING[@]} -ne 0 ]; then
    echo "Following packages are missing, please install them first."
    echo ${MISSING[*]}
    exit 1
fi

APPNAME=InterviewRestBusinessSeconds
GROUPNAME=webapps
# app folder in /webapps/<appname>_project
APPFOLDER=$APPNAME
APPFOLDERPATH=/$GROUPNAME/$APPFOLDER

PYTHON_VER_STR=`python3 -c 'import sys; ver = "{0}.{1}".format(sys.version_info[:][0], sys.version_info[:][1]); print(ver)'`

# Verify python version
echo "Python ver: $PYTHON_VER_STR"

ERROR=False
echo "Creating InterviewRestBusinessSeconds folder '$APPFOLDERPATH'."
mkdir -p /$GROUPNAME/$APPFOLDER || ERROR=True

if [ ERROR == True ]; then
    echo "Could not create app folder"
    exit 1
fi

# Check group 'webapps' exists, and if it doesn't create it
ERROR=False
getent group $GROUPNAME
if [ $? -ne 0 ]; then
    echo "Creating group '$GROUPNAME'."
    groupadd --system $GROUPNAME || ERROR=True
fi

if [ ERROR == True ]; then
    echo "Could not create group 'webapps'"
    exit 1
fi

# create the app user account
ERROR=False
grep "$APPNAME:" /etc/passwd
if [ $? -ne 0 ]; then
    echo "Creating user account '$APPNAME'..."
    useradd --system --gid $GROUPNAME --shell /bin/bash --home $APPFOLDERPATH $APPNAME || ERROR=True
fi

if [ ERROR == True ]; then
    echo "Could not create automation user account '$APPNAME'"
    exit 1
fi

# change ownership of the app folder to the newly created user account
ERROR=False
echo "Setting ownership of $APPFOLDERPATH and its descendents to $APPNAME:$GROUPNAME..."
chown -R $APPNAME:$GROUPNAME $APPFOLDERPATH || ERROR=True

if [ ERROR == True ]; then
    echo "Error setting ownership"
    exit 1
fi

# give group execution rights in the folder;
ERROR=False
chmod g+x $APPFOLDERPATH || ERROR=True

if [ ERROR == True ]; then
    echo "Error setting group execute flag"
    exit 1
fi

# Install python virtualenv in the APPFOLDER
ERROR=False
echo "Creating environment setup for django app..."
su -l $APPNAME << 'EOF'
pwd
echo "Setting up python virtualenv..."
virtualenv -p python3 . || ERROR=True

if [ ERROR == True ]; then
    echo "Error installing Python 3 virtual environment to app folder"
    exit 1
fi
EOF

# The new app specific virtual environment:
su -l $APPNAME << 'EOF'
source ./bin/activate
# upgrade pip
ERROR=False
pip install --upgrade pip || ERROR=True

if [ ERROR == True ]; then
    echo "Error upgrading pip to the latest version."
    exit 1
fi

# install prerequisite python packages for a django app using pip
ERROR=False
echo "Installing Python requirements.txt."
pip3 install -r requirements.txt || ERROR=True

if [ ERROR == True ]; then
    echo "Error Installing Python requirements.txt."
    exit 1
fi

ERROR=False
echo "Installing gunicorn."
pip3 install gunicorn || ERROR=True

if [ ERROR == True ]; then
    echo "Error Installing gunicorn."
    exit 1
fi

ERROR=False
echo "Installing setproctitle."
pip3 install setproctitle || ERROR=True

if [ ERROR == True ]; then
    echo "Error Installing setproctitle."
    exit 1
fi

# create the default folders where we store django app's resources
ERROR=False
echo "Creating static file folders..."
mkdir logs nginx run static || ERROR=True

if [ ERROR == True ]; then
    echo "Error creating static folders"
    exit 1
fi

# Create the UNIX socket file for WSGI interface
echo "Creating WSGI interface UNIX socket file..."
python -c "import socket as s; sock = s.socket(s.AF_UNIX); sock.bind('./run/gunicorn.sock')"
EOF

# Create the script that will init the virtual environment. This
# script will be called from the gunicorn start script created next.
echo "Creating virtual environment setup script..."
cat > /tmp/prepare_env.sh << EOF
DJANGODIR=$APPFOLDERPATH/$APPNAME          # Django project directory

export DJANGO_SETTINGS_MODULE=$APPNAME.settings # settings file for the app
export PYTHONPATH=\$DJANGODIR:\$PYTHONPATH

cd $APPFOLDERPATH
source ./bin/activate
EOF

mv /tmp/prepare_env.sh $APPFOLDERPATH
chown $APPNAME:$GROUPNAME $APPFOLDERPATH/prepare_env.sh

# Create gunicorn start script which will be spawned and managed
# using supervisord.
echo "Creating gunicorn startup script..."
cat > /tmp/gunicorn_start.sh << EOF
#!/bin/bash

cd $APPFOLDERPATH
source ./prepare_env.sh

SOCKFILE=$APPFOLDERPATH/run/gunicorn.sock  # we will communicte using this unix socket
USER=$APPNAME                                        # the user to run as
GROUP=$GROUPNAME                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_WSGI_MODULE=$APPNAME.wsgi                     # WSGI module name

echo "Starting $APPNAME as \`whoami\`"

# Create the run directory if it doesn't exist
RUNDIR=\$(dirname \$SOCKFILE)
test -d \$RUNDIR || mkdir -p \$RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ./bin/gunicorn \${DJANGO_WSGI_MODULE}:application \
  --name $APPNAME \
  --workers \$NUM_WORKERS \
  --user=\$USER --group=\$GROUP \
  --bind=unix:\$SOCKFILE \
  --log-level=debug \
  --log-file=-
EOF

# Move the script to app folder
mv /tmp/gunicorn_start.sh $APPFOLDERPATH
chown $APPNAME:$GROUPNAME $APPFOLDERPATH/gunicorn_start.sh
chmod u+x $APPFOLDERPATH/gunicorn_start.sh

# Create nginx template in $APPFOLDERPATH/nginx
mkdir -p $APPFOLDERPATH/nginx
APPSERVERNAME=$APPNAME
APPSERVERNAME+=_gunicorn
cat > $APPFOLDERPATH/nginx/$APPNAME.conf << EOF
upstream $APPSERVERNAME {
    server unix:$APPFOLDERPATH/run/gunicorn.sock fail_timeout=0;
}
server {
    listen 80;
    server_name $DOMAIN;

    client_max_body_size 5M;
    keepalive_timeout 5;
    underscores_in_headers on;

    access_log $APPFOLDERPATH/logs/nginx-access.log;
    error_log $APPFOLDERPATH/logs/nginx-error.log;

    location /static {
        alias $APPFOLDERPATH/static;
    }
    location / {
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header Host \$http_host;
        proxy_redirect off;
        proxy_pass http://$APPSERVERNAME;
    }
}
EOF

# make a symbolic link to the nginx conf file in sites-enabled
ln -sf $APPFOLDERPATH/nginx/$APPNAME.conf /etc/nginx/sites-enabled/$APPNAME

# Setup supervisor

# Copy supervisord.conf if it does not exist
ERROR=False
if [ ! -f /etc/supervisord.conf ]; then
	cp ./supervisord.conf /etc || ERROR=True
fi

if [ ERROR == True ]; then
    echo "Error copying supervisord.conf"
    exit 1
fi

# Create the supervisor application conf file
mkdir -p /etc/supervisor
cat > /etc/supervisor/$APPNAME.conf << EOF
[program:$APPNAME]
command = $APPFOLDERPATH/gunicorn_start.sh
user = $APPNAME
stdout_logfile = $APPFOLDERPATH/logs/gunicorn_supervisor.log
redirect_stderr = true
EOF

SUPERVISORD_ACTION='reload'
# Create supervisord init.d script that can be controlled with service


if [ ! -f /etc/init.d/supervisord ]; then
    echo "Setting up supervisor to autostart during bootup..."
    ERROR=False
    cp ./supervisord /etc/init.d || ERROR=True

    if [ ERROR == True ]; then
        echo "Error copying /etc/init.d/supervisord"
        exit 1
    fi

    # enable execute flag on the script
    ERROR=False
    chmod +x /etc/init.d/supervisord || ERROR=True

    if [ ERROR == True ]; then
        echo "Error setting execute flag on supervisord"
        exit 1
    fi

    # create the entries in runlevel folders to autostart supervisord
    ERROR=False
    update-rc.d supervisord defaults || ERROR=True

    if [ ERROR == True ]; then
        echo "Error configuring supervisord to autostart"
        exit 1
    fi

    SUPERVISORD_ACTION='start'
fi

# Now create a django project that can be run using a GUnicorn script
echo "Copy django project..."
su -l $APPNAME << EOF
source ./bin/activate
rsync -raz --progress --omit-dir-times $CURRENT_APP_PATH $APPFOLDERPATH/$APPNAME/
EOF

# change ownership of the app folder to the newly created user account
ERROR=False
echo "Setting ownership of $APPFOLDERPATH and its descendents to $APPNAME:$GROUPNAME..."
chown -R $APPNAME:$GROUPNAME $APPFOLDERPATH || ERROR=True

if [ ERROR == True ]; then
    echo "Error setting ownership"
    exit 1
fi

# Run Python tests
cd $APPFOLDERPATH
source ./bin/activate
EOF
pytest
EOF

# Reload/start supervisord and nginx
# Start/reload the supervisord daemon
service supervisord status > /dev/null
if [ $? -eq 0 ]; then
    # Service is running, restart it
    ERROR=False
    service supervisord restart || ERROR=True

    if [ ERROR == True ]; then
        echo "Error restarting supervisord"
        exit 1
    fi
else
    # Service is not running, probably it's been installed first. Start it
    ERROR=False
    service supervisord start || ERROR=True

    if [ ERROR == True ]; then
        echo "Error starting supervisord"
        exit 1
    fi
fi

# Reload nginx so that requests to domain are redirected to the gunicorn process
ERROR=False
nginx -s reload || ERROR=True

if [ ERROR == True ]; then
    echo "Error reloading nginx. Check configuration files"
    exit 1
fi

echo "Complete."
