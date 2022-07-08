from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('group_list.html/', views.group_posts),
    path('group/<slug:slug>/', views.group),
] 