from random import randint
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count
from .forms import QuestionForm
from .models import Cocktail, Material

# Create your views here.


def _get_one_item_randomly(model):
    """指定モデルからランダムに１件取得する"""
    count = model.objects.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    return model.objects.all()[random_index]


def _check_answer(cocktail, choiced_materials):
    """答え合わせ"""
    # 結果のデフォルト値(不正解)
    result = {'text': '不正解です', 'css-class': 'text-danger'}
    answer_item_css = {}
    match_counter = 0

    cocktail_materials = cocktail.materials.all()
    for material in cocktail_materials:
        if material in choiced_materials:
            match_counter += 1
            answer_item_css[material.pk] = 'list-group-item-success'
        else:
            answer_item_css[material.pk] = 'list-group-item-danger'
    if match_counter == len(choiced_materials):
        result['text'] = '正解です'
        result['css-class'] = 'text-success'
    result['answer-css-set'] = answer_item_css
    return result


def top(request):
    """トップページのビュー"""
    return render(request, 'learn_cocktail/top.html')


def question(request):
    """問題ページのビュー"""
    form = QuestionForm()
    cocktail = _get_one_item_randomly(Cocktail)
    return render(request, 'learn_cocktail/question.html', {
        'form': form,
        'question_cocktail': cocktail,
    })


def answer(request):
    """回答結果ページのビュー"""
    q_cocktail = Cocktail.objects.get(pk=request.POST.get('q_cocktail'))
    mats = request.POST.getlist('choice_materials')
    choiced_materials = Material.objects.in_bulk(id_list=mats,
                                                 field_name='pk')
    result = _check_answer(q_cocktail, choiced_materials)
    return render(request, 'learn_cocktail/answer.html', {
        'q_cocktail': q_cocktail,
        'choiced_materials': choiced_materials,
        'result_txt': result['text'],
        'result_css_cls': result['css-class'],
        'answer_item_css_cls': result['answer-css-set'],
    })
