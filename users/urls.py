from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('start/', views.startPage, name="start"),
    path('logout/', views.logoutUser, name="logout"),
]
