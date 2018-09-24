from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    #xurl(r'^/detail$',views.detail,name='detail'),
    url(r'^search/$', views.search, name='detail'),
    url(r'^search/ques/(?P<string>[\w\-]+):/$', views.ans, name='ans'),
]
