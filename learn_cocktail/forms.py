from django import forms
from .models import Material


class QuestionForm(forms.Form):
    # materials = [{'pk': mat.pk, 'name': mat.name}
    #              for mat in Material.objects.order_by('kind').all()]

    cocktail = forms.CharField()
    choice_materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.order_by('kind').all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'd-none',
            'autocomplete': "off"}),
        # require=True,
    )
