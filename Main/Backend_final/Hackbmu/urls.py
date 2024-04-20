from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('mainpage/',views.mainpage,name='mainpage')
]