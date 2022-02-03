from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # displays all available blogs
    path("<str:name>", views.blog_post)# handles any specific blogpost
]