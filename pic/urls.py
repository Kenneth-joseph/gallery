from django.conf.urls import url
from django.shortcuts import render
from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^search/', views.search_results, name='search_results')

]
