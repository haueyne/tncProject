from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'cocktail/index.html')


def top(request):
    return render(request, 'cocktail/top.html')
