# coding: utf8
from django.conf.urls import url
from . import views
from  django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    url('^contact$', views.contact, name='contact'),
    url('^about$', views.about, name='about'),
    url('^$', views.post_list, name='post_list'),
    url(r'^(?P<id>\d+)', DetailView.as_view(model=Post, template_name="justapost.html")),

]