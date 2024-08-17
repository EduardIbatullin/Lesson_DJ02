from django.shortcuts import render


def index(request):
    return render(request, 'books/index.html')


def about(request):
    return render(request, 'books/about.html')


def foundation(request):
    return render(request, 'books/foundation.html')


def robot_series(request):
    return render(request, 'books/robot_series.html')
