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
            messages.success(request, 'Konto zostało utworzono. Zaloguj się. ')
            return redirect('login')

    context = {'form':form}
    return render(request, 'users/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('start_u')
			else:
				messages.info(request, 'ID użytkownika lub hasło jest niepoprawne')

		context = {}
		return render(request, 'users/login.html', context)

@login_required(login_url='login')
def startPage(request):
    courtfiles_list = CourtFile.objects.all()
    context = {'courtfiles_list': courtfiles_list}
    
    return render(request, 'users/start_u.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


