from django.shortcuts import redirect
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('contacts/', views.contacts, name='contacts'),
    path('topic/<int:topic_id>/', views.newstext, name='newstext'),
]
