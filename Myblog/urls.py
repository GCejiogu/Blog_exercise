from django.contrib import admin
from django.urls import path
from .views import HomeView

urlpatterns = [
    path("Home/",HomeView.as_view()),
]
