# Interview Rest Business Seconds API
Rest API to calculate Business Seconds for an Interview


## Hendrik de Wilde


## Assignment
Provide an API end point that will calculate the total number of business seconds between two given times.
A business second is defined as any whole second that elapses after 08:00 and before 17:00 during
a weekday (Monday - Friday) that is not a public holiday in the Republic of South Africa.
The end point must support only list GET requests and must take two parameters: start_time and end_time.
Parameter values will be in ISO-8601 format.
You are guaranteed that start_time will be before end_time.
The end point must respond with only a single integer value for successful requests or
a suitable error message string for failed requests.

The repository should show your development workflow.
The repository should include all code for the end point as well as a script which automates deployment.
You should also include automated testing in the repository.

- Include the end point's URL in your submission
- Complete in python
- Do not use a package to calculate business seconds


## Note
ISO 8601 FORMAT:
Standard is an International Standard for the representation of dates and times.
This format contains date, time, and the offset from UTC, as well as the T character that
designates the start of the time, for example, 2007-04-05T12:30:22-02:00


## Required
Python 3.6


## Packages Install
```pip install -r requirements.txt```


## End point's URL
```/api/business_seconds/?start_time=2021-03-28T08:00:00-0200&end_time=2021-03-29T08:00:01-0200```


## Install Script
Must be installed op Ubuntu 18.04.

```cd ~```

Git clone https://github.com/hendrikdewilde/InterviewRestBusinessSeconds.git

```django_deploy_project.sh [<python-version>] [<domain-name>] [<current-app-path>]```

Example: ```django_deploy_project.sh 3 mydomain.co.za /home/ubuntu/InterviewRestBusinessSeconds/```


## Tests
```pytest tests/test_Api/test_serializers.py```

```pytest tests/test_Api/test_views.py```

```pytest```