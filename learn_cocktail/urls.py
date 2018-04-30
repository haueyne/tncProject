from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='learn_cocktail/index.html'), name='top'),
    path('', views.top, name='top'),
    path('question/', views.question, name='question'),
    path('answer/', views.answer, name='answer'),
]
