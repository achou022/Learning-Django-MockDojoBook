from django.urls import path
from . import views

urlpatterns=[
    path('', views.wall),
    path('/post', views.createPost),
    path('/post/comment', views.createComment),
    path('/post/destroy', views.destroy)
]