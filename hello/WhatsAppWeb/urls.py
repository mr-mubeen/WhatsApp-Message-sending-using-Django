from django.contrib import admin
from django.urls import path
from WhatsAppWeb import views
import WhatsAppWeb

urlpatterns = [
       path('', views.index , name = "home"),
]
