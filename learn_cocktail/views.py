from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm
from .models import Cocktail

# Create your views here.


def top(request):
    """トップページのビュー"""
    return render(request, 'learn_cocktail/top.html')


def question(request):
    """問題ページのビュー"""
    form = QuestionForm()
    # TODO この方法は遅いため、別の方法を作成する
    cocktail = Cocktail.objects.order_by('?').first()
    return render(request, 'learn_cocktail/question.html',{
        'form': form,
        'question_cocktail': cocktail,
    })

def answer(request):
    """回答結果ページのビュー"""
    question_cocktail = request.POST.get('question')
    choices_materials = request.POST.getlist('materials')
    return render(request, 'learn_cocktail/answer.html', {
        'cocktail': question_cocktail,
        'choiced_materials': choice_materials,
    })
