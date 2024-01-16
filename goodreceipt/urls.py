from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('grncreated',views.GRNView.as_view()),
    path('grncreated/<int:pk>/',views.GRNView.as_view())
   
]