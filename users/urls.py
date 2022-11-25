from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('start_u/', views.startPage, name="start_u"),
    path('logout/', views.logoutUser, name="logout"),
]

urlpatterns += staticfiles_urlpatterns()
