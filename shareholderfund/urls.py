from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index),
    # share fund 
    path('shname', views.ShreHolderNameView.as_view()),
    path('shname/<int:pk>/', views.ShreHolderNameView.as_view()),
    path('shfund', views.ShreHolderFundView.as_view()),
    path('shfund/<int:pk>/', views.ShreHolderFundView.as_view()),
    path('shfund/<int:pk>/', views.ShreHolderFundView.as_view()),
    path('capialDisview',views.CapitalDisclouserview.as_view()),
    

    # rd person ursls 
    path('rdname',views.RdName.as_view()),
    path('rdname/<int:pk>',views.RdName.as_view()),
    path('rdcoll',views.RDCollectionBulkCreateView.as_view()),
    path('rdcoll/<int:pk>',views.RDCollectionBulkCreateView.as_view()),
    path('rdDataView',views.RDDataAPIView.as_view()),

    # loan person urls 
    path('loanname',views.LoanName.as_view()),
    path('loanname/<int:pk>',views.LoanName.as_view()),
    path('loancoll',views.LoanCollectionBulkCreateView.as_view()),
    path('loancoll/<int:pk>',views.LoanCollectionBulkCreateView.as_view()),
    path('loanDataView',views.LoanDataAPIView.as_view()),
    path('loanamount',views.LaonAmountView.as_view()),
    path('loanamount/<int:pk>',views.LaonAmountView.as_view()),

     #Rdintrest 
    path('rdintrest',views.RDintrestView.as_view()),
    path('rdintrest/<int:pk>',views.RDintrestView.as_view()),

    # RDcollectionNewserilizer 
    path('rdcollectionnew',views.RDcollectionNewView.as_view()),
    path('rdcollectionnew/<int:pk>',views.RDcollectionNewView.as_view()),
    path('rdDataNewView',views.RDDataNewAPIView.as_view()),
    path('orignalrdcollectionnew/<int:pk>',views.OrignalRDcollectionNewView.as_view()),
]