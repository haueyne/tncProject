from django import forms
from .models import Material


class QuestionForm(forms.Form):
    materials = [(mat.pk, mat.name) for mat in Material.objects.all()]

    cocktail = forms.CharField()
    choice_materials = forms.CharField(widget=forms.Select(choices=materials))
