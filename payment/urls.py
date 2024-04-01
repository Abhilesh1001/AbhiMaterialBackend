
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('', views.index),
    # Advance Payment 
     path('adpayment', views.AdvancePaymaentView.as_view()),
     path('adpayment/<int:pk>/', views.AdvancePaymaentView.as_view()),
    #  payment to vendor 
    path('payment', views.PaymaentView.as_view()),
    path('payment/<int:pk>/', views.PaymaentView.as_view()),

    path('paymnetbymiro',views.PaymentFilterByMiro.as_view())
]
