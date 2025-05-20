from django.shortcuts import redirect
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('contacts/', views.contacts, name='contacts'),
    path('topic/<int:topic_id>/', views.newstext, name='newstext'),


# авторизация и регистрация пользователей
    re_path('^register/$', views.RegisterFormView.as_view()),
    re_path('^login/$', views.LoginFormView.as_view()),
    re_path('^logout/$', views.LogoutView.as_view()),
    re_path('^password-change/', views.PasswordChangeView.as_view())

]
