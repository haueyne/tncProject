from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('question/', views.question, name='question'),
    path('answer/', views.answer, name='answer'),
]
