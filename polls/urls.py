from django.conf.urls import url
from django.urls import path, re_path
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # 对你的URL进行命名，可以让你能够在Django的任意处，尤其是模板内显式地引用它。
    # 相当于给URL取了个全局变量名，你只需要修改这个全局变量的值，在整个Django中引用它的地方也将同样获得改变
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
