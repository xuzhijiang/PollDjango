from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^link/$', views.link, name='link'),
    url(r'^message$', views.message, name='message'),
    url(r'^article/(?P<pk>\d+)/$', views.articles, name='article'),
    url(r'^get_comment/$', views.get_comment, name='get_comment'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^tag/(?P<name>.*?)/$', views.tag, name='tag'),
]
