from django import template

register = template.Library()


@register.filter
def get_dict_value(value, arg, default=''):
    """テンプレート内で辞書型に変数でアクセスするための関数"""
    if arg in value:
        return value[arg]
    else:
        return default
