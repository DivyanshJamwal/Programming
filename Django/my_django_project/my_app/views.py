from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def technology(request):
    return render(request, 'news/technology.html')

def politics(request):
    return render(request, 'news/politics.html')

def sports(request):
    return render(request, 'news/sports.html')

def entertainment(request):
    return render(request, 'news/entertainment.html')