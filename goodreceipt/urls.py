from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('grncreated',views.GRNView.as_view()),
    path('grncreated/<int:pk>/',views.GRNView.as_view()),
    path('grnview/<int:pk>/',views.OrGRNView.as_view()),

    # miro 
    path('mirocreate',views.MiroView.as_view()),
    path('mirocreated/<int:pk>/',views.MiroView.as_view()),

    # IRN PO Insert 
    path('irnpoinsert/<int:pk>/',views.POinINRView.as_view()),

    # materialIssue    
    path('materialissuecreate',views.MaterialIssueView.as_view()),
    path('materialissuecreate/<int:pk>/',views.MaterialIssueView.as_view()),
    
    
    
   
   
]