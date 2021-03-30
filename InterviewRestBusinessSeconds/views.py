import logging

from django.shortcuts import render

log = logging.getLogger(__name__)


def index(request):
    return render(request, 'index.html', {})
