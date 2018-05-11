import numpy as np
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import QuestionForm
from .models import Cocktail, Material

# Create your views here.


def get_weighted_item_randomly(model, extract_num=1, weighted_field='importance'):
    """指定モデルから重み付けランダム抽出を行う

    :param model: 対象モデル
    :param extract_num: 抽出数
    :param weighted_field: 重み付け定義しているフィールド
    :return: nmpy.ndarray
    """
    total_importance = model.objects.aggregate(Sum(weighted_field))[weighted_field + '__sum']
    weighted = [item[weighted_field] / total_importance
                for item in model.objects.values(weighted_field)]
    extract_num = extract_num if extract_num <= len(weighted) else weighted
    return np.random.choice(model.objects.all(), extract_num, replace=True, p=weighted)


def _check_answer(cocktail, choiced_materials):
    """答え合わせ"""
    # 結果のデフォルト値(不正解)
    result = {'text': '不正解です', 'css-class': 'text-danger'}
    answer_item_css = {}
    icon = {}
    match_counter = 0

    cocktail_materials = cocktail.materials.all()
    for material in cocktail_materials:
        if material in choiced_materials:
            match_counter += 1
            answer_item_css[material.pk] = 'list-group-item-success'
            icon[material.pk] = 'check'
        else:
            answer_item_css[material.pk] = 'list-group-item-danger'
            icon[material.pk] = 'error'
    if match_counter == len(cocktail_materials):
        result['text'] = '正解です'
        result['css-class'] = 'text-success'
    result['answer-css-set'] = answer_item_css
    result['icon'] = icon
    return result


def calc_cocktail_alcohol(cocktail, round_digit=2):
    """指定カクテルのアルコール度数を計算して取得

    :param round_digit: アルコール度数を四捨五入する小数点桁数
    """
    total_amount = 0
    alcohol = 0
    for recipe in cocktail.recipe_set.all():
        total_amount += recipe.quantity
        alcohol += recipe.quantity * recipe.material.alc_percent
    alc_percent = alcohol / total_amount
    return round(alc_percent, round_digit)


def top(request):
    """トップページのビュー"""
    return render(request, 'learn_cocktail/top.html')


def question(request):
    """問題ページのビュー"""
    form = QuestionForm()
    cocktail = get_weighted_item_randomly(Cocktail)[0]
    return render(request, 'learn_cocktail/question.html', {
        'form': form,
        'question_cocktail': cocktail,
    })


def answer(request):
    """回答結果ページのビュー"""
    q_cocktail = Cocktail.objects.get(pk=request.POST.get('q_cocktail'))
    choiced_materials = Material.objects.filter(
        id__in=request.POST.getlist('choice_materials'))
    ans_result = _check_answer(q_cocktail, choiced_materials)
    alc_percent = calc_cocktail_alcohol(q_cocktail)
    return render(request, 'learn_cocktail/answer.html', {
        'q_cocktail': q_cocktail,
        'q_alc_percent': alc_percent,
        'choiced_materials': choiced_materials,
        'result_txt': ans_result['text'],
        'result_css_cls': ans_result['css-class'],
        'answer_item_css_cls': ans_result['answer-css-set'],
        'answer_result_icon': ans_result['icon'],
    })


def cocktail_list(request):
    cocktail_objs = Cocktail.objects.all()
    paginator = Paginator(cocktail_objs, 10)  # show 10 cocktails per page

    page = request.GET.get('page', '1')
    cocktails = paginator.get_page(page)
    return render(request, 'learn_cocktail/cocktail_list.html', {
        'cocktails': cocktails,
    })
