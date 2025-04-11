
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('about/', views.about, name="about"),
    path('room/<str:pk>/', views.room, name="room"),
]
