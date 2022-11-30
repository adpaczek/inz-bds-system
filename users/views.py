from contextvars import Context
from pdb import post_mortem
from sunau import Au_read
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .models import CourtFile
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

def home(request):
    context= {}
    return render(request, 'users/home.html', context)

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST' :                   
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Konto zostało utworzone. Zaloguj się. ')
            return redirect('login')

    context = {'form':form}
    return render(request, 'users/register.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('start_a')
			else:
				messages.info(request, 'ID użytkownika lub hasło jest niepoprawne.')

	context = {}
	return render(request, 'users/login.html', context)

@login_required(login_url='login')
def startPage(request):
    courtfiles_list = CourtFile.objects.all()
    context = {'courtfiles_list': courtfiles_list}
    
    return render(request, 'users/start_u.html', context)

@login_required(login_url='login')
@admin_only
def astartPage(request):
    context = {}
    return render(request, 'users/start_a.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def bazabPage(request):
    context = {}
    return render(request, 'users/baza_b.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def bazaobPage(request):
    context = {}
    return render(request, 'users/baza_ob.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def infoPage(request):
    context = {}
    return render(request, 'users/info.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def pomocPage(request):      
    context = {}
    return render(request, 'users/pomoc.html', context)   

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def abazabPage(request):
    context = {}
    return render(request, 'users/baza_b.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def abazaobPage(request):
    context = {}
    return render(request, 'users/a_ob.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def ainfoPage(request):
    context = {}
    return render(request, 'users/a_info.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def apomocPage(request):      
    context = {}
    return render(request, 'users/a_pomoc.html', context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def prosbyPage(request):      
    context = {}
    return render(request, 'users/prosby.html', context) 

