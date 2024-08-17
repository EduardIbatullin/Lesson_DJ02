from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'app_lw_DJ02/index.html')


def new(request):
    return render(request, 'app_lw_DJ02/new.html')
