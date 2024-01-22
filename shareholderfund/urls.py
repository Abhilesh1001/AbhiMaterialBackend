

from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    path('shname', views.ShreHolderNameView.as_view()),
    path('shname/<int:pk>/', views.ShreHolderNameView.as_view()),
    path('shfund', views.ShreHolderFundView.as_view()),
    path('shfund/<int:pk>/', views.ShreHolderFundView.as_view()),
    path('shfund/<int:pk>/', views.ShreHolderFundView.as_view()),
    path('capialDisview',views.CapitalDisclouserview.as_view()),
    path('rdname',views.RdName.as_view()),
    path('rdname/<int:pk>',views.RdName.as_view()),
    path('rdcoll',views.RDCollectionBulkCreateView.as_view()),
    path('rdcoll/<int:pk>',views.RDCollectionBulkCreateView.as_view()),
]