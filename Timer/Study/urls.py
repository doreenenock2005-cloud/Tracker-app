from django.http import HttpResponse
from django.urls import path 
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
from Study import views

def home(request):
    return HttpResponse("Welcome to the Study Tracker API")


urlpatterns = [
    path('',home),
    path('user', views.user), 
    path('api-token-auth/', obtain_auth_token),
  
]
