from django.urls import path 
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from .import views

urlpatterns = [
    path('user', views.user), 
    path('api-token-auth/', obtain_auth_token),
  
]
