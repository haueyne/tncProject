from django import template
from ..views import calc_cocktail_alcohol

register = template.Library()


@register.filter
def get_dict_value(value, arg, default=''):
    """テンプレート内で辞書型に変数でアクセスするための関数"""
    if arg in value:
        return value[arg]
    else:
        return default


@register.filter
def get_alc_percent(cocktail):
    """テンプレート内でカクテルのアルコール度数を計算"""
    return calc_cocktail_alcohol(cocktail)
