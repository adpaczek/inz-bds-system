from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('start_u/', views.startPage, name="start_u"),
    path('start_a/', views.astartPage, name="start_a"),
    path('logout/', views.logoutUser, name="logout"),
    path('baza_b/', views.bazabPage, name="baza_b"),
    path('baza_ob/', views.bazaobPage, name="baza_ob"),
    path('pomoc/', views.pomocPage, name="pomoc"),
    path('info/', views.infoPage, name="info"),
    path('a_baza_b/', views.abazabPage, name="a_baza_b"),
    path('a_ob/', views.abazaobPage, name="a_ob"),
    path('a_pomoc/', views.apomocPage, name="a_pomoc"),
    path('a_info/', views.ainfoPage, name="a_info"),
    path('prosby/', views.prosbyPage, name="prosby"),
    path('ocr/', views.prosbyPage, name="ocr"),
    path('podglad/<list_id>', views.podgladPage, name="podglad"),
    path('dodawanie/', views.dodawaniePage, name="dodawanie"),
    path('teczka/<teczka_id>', views.teczkaPage, name="teczka"),
    path('a_podglad/<podglad_id>', views.apodgladPage, name="a_podglad"),
    path('usuwanieT/<delete_id>', views.usuwanieTeczki, name="usuwanieT"),
    path('usuwanieP/<delete_id>', views.usuwanieProsby, name="usuwanieP"),
    path('access/<access_id>', views.accessView, name="access"),
    path('biegly/<biegly_id>', views.bieglyPage, name="biegly"),
    path('a_biegly/<biegly_id>', views.abieglyPage, name="a_biegly"),
]

urlpatterns += staticfiles_urlpatterns()

