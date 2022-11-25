from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('start_u/', views.startPage, name="start_u"),
    path('logout/', views.logoutUser, name="logout"),
    path('baza_b/', views.bazabPage, name="baza_b"),
    path('baza_ob/', views.bazaobPage, name="baza_ob"),
    path('pomoc/', views.pomocPage, name="pomoc"),
    path('info/', views.infoPage, name="info"),
]

urlpatterns += staticfiles_urlpatterns()
