from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('creatematerial', views.MaterialView.as_view()),
    path('creatematerial/<int:pk>/', views.MaterialView.as_view()),
    path('createpurchase', views.PurchaseRequestNewView.as_view()),
    path('createpurchase/<int:pk>/', views.PurchaseRequestNewView.as_view()),
    path('createvender', views.VendorView.as_view()),
    path('createvender/<int:pk>/', views.VendorView.as_view()),
    path('createDelivery', views.DeliveryAdressView.as_view()),
    path('createDelivery/<int:pk>/', views.DeliveryAdressView.as_view()),
    path('createpo', views.PurchaseOrderView.as_view()),
    path('createpo/<int:pk>/', views.PurchaseOrderView.as_view()),
    path('prview/<int:pk>/', views.OrPurchaseRequestNewView.as_view()),
]