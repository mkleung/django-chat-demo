
from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    
    # Room
    path('about/', views.about, name="about"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    # polls
    path('polls/', views.polls, name="polls"),
    path("polls/<int:question_id>/", views.detail, name="detail"),
    path("polls/<int:question_id>/results/", views.results, name="results"),
    path("polls/<int:question_id>/vote/", views.vote, name="vote"),

    # Authentication
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
]
