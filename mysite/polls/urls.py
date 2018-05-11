from django.conf.urls import url
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path('^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
