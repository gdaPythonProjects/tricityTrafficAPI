from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def cron(request):
    return HttpResponse('cron')
