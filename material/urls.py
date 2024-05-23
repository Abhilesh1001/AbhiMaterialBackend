from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # create material 
    path('creatematerial', views.MaterialView.as_view()),
    path('creatematerial/<int:pk>/', views.MaterialView.as_view()),

    # create Purchase 
    path('createpurchase', views.PurchaseRequestNewView.as_view()),
    path('createpurchase/<int:pk>/', views.PurchaseRequestNewView.as_view()),

    # create Vendor 
    path('createvender', views.VendorView.as_view()),
    path('createvender/<int:pk>/', views.VendorView.as_view()),

    # create delivery 
    path('createDelivery', views.DeliveryAdressView.as_view()),
    path('createDelivery/<int:pk>/', views.DeliveryAdressView.as_view()),

    # create Purchse Order 
    path('createpo', views.PurchaseOrderView.as_view()),
    path('createpo/<int:pk>/', views.PurchaseOrderView.as_view()),

    # orignasl prview 
    path('prview/<int:pk>/', views.OrPurchaseRequestNewView.as_view()),
    path('purchaseorderadvance/<int:pk>',views.PurchaseOrderAdvance.as_view()),

    # orignal poview 
    path('poview/<int:pk>/', views.OrPuchaseOrderView.as_view()),

    # Materil Unit 
    path('materialgroup',views.MaterialGroupView.as_view()),
    path('materialgroup/<int:pk>/',views.MaterialGroupView.as_view()),

    # Materil Group 
    path('materialunit',views.MaterialUnitView.as_view()),
    path('materialunit/<int:pk>/',views.MaterialUnitView.as_view()),


    

]