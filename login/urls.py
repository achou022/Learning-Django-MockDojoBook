from django.urls import path
from . import views

urlpatterns=[
    path('', views.login),
    path('success', views.success),
    path('register', views.register),
    path('login', views.loginValidation),
    path('logout', views.logout)
]