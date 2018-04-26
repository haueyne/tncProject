from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def top(request):
    return render(request, 'learn_cocktail/top.html')


def question(request):
    return render(request, 'learn_cocktail/question.html')

def answer(request):
    return render(request, 'learn_cocktail/answer.html')
