from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^index$', views.index, name='index'),  # urlとviewの結びつけ
    url(r'^$', views.top, name='top'),
]
