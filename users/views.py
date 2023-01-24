from audioop import reverse
from contextvars import Context
from pdb import post_mortem
import queue
from sunau import Au_read
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CourtfileForm, FileForm, UploadForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .models import CourtFile, ExpertsStatement, Expert, AccessRequest, File
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import FormView


#from io import BytesIO
#from reportlab.pdfgen import canvas

import pytesseract  
from PIL import Image

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
#path_wkhtmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

tessdata_dir_config = '--tessdata-dir "C:\Program Files\\Tesseract-OCR\\tessdata"'

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
@allowed_users(allowed_roles=['user'])
def startPage(request):
    courtfiles_list = CourtFile.objects.all()
    access_list = AccessRequest.objects.filter(user=request.user)
    context = {'courtfiles_list': courtfiles_list, 'access_list': access_list}
    
    return render(request, 'users/start_u.html', context)

@login_required(login_url='login')
@admin_only
def astartPage(request):
    courtfiles_list = CourtFile.objects.all()
    current_user = request.user
    context = {'courtfiles_list': courtfiles_list}
    return render(request, 'users/start_a.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def bazabPage(request):
    experts_list = Expert.objects.all()
    context = {'experts_list': experts_list}
    return render(request, 'users/baza_b.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def bazaobPage(request):    
    estatements_list = ExpertsStatement.objects.all()
    context = {'estatements_list': estatements_list}
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
@allowed_users(allowed_roles=['user'])
def podgladPage(request, list_id): 
    pdf_file = CourtFile.objects.get(pk=list_id).contents_list
    response = HttpResponse(pdf_file, content_type='application/pdf')    
    response['Content-Disposition'] = 'inline; filename=spis.pdf'
    return response   

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def apodgladPage(request, podglad_id): 
    pdf_file = CourtFile.objects.get(pk=podglad_id).contents_list
    response = HttpResponse(pdf_file, content_type='application/pdf')    
    response['Content-Disposition'] = 'inline; filename=spis.pdf'
    return response      

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def abazabPage(request):
    experts_list = Expert.objects.all()
    context = {'experts_list': experts_list}
    return render(request, 'users/a_baza_b.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def abazaobPage(request):
    estatements_list = ExpertsStatement.objects.all()
    context = {'estatements_list': estatements_list}
    return render(request, 'users/a_ob.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def ainfoPage(request):
    context = {}
    return render(request, 'users/a_info.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def aocrPage(request):
    context = {}
    return render(request, 'users/ocr.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def apomocPage(request):      
    context = {}
    return render(request, 'users/a_pomoc.html', context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def prosbyPage(request):
    request_list = AccessRequest.objects.all()      
    context = {'request_list': request_list}
    return render(request, 'users/prosby.html', context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def dodawaniePage(request):  
    if request.method == 'POST':
        form = CourtfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('start_a')
    else: 
        form = CourtfileForm()
    return render(request, 'users/dodawanie.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def teczkaPage(request, teczka_id):  
    teczka = CourtFile.objects.get(pk=teczka_id)
    pliki = File.objects.all()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else: 
        form = FileForm()
    return render(request, 'users/teczka.html', {'teczka': teczka, 'form': form, 'pliki': pliki})

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def usuwanieTeczki(request, delete_id):
    data = CourtFile.objects.get(pk=delete_id)
    data.delete()
    return redirect('start_a')

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def usuwanieProsby(request, delete_id):
    data = AccessRequest.objects.get(pk=delete_id)
    data.delete()
    return redirect('prosby')

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def acceptPage(request, accept_id):
    AccessRequest.objects.filter(pk=accept_id).update(status="zaakceptowana")
    return redirect('prosby')

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def sendingPage(request, send_id):
    access_request = CourtFile.objects.get(pk=send_id)
    print(access_request)
    AccessRequest.objects.create(user=request.user, signature=access_request)    
    return redirect('start_u')

@login_required(login_url='login')
@allowed_users(allowed_roles=['user'])
def bieglyPage(request, biegly_id): 
    profile = Expert.objects.get(pk=biegly_id)
    statements = ExpertsStatement.objects.filter(expert_id=biegly_id)   
    context = {'profile' : profile, 'statements': statements}
    return render(request, 'users/biegly.html', context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['archiwizator'])
def abieglyPage(request, biegly_id):  
    profile = Expert.objects.get(pk=biegly_id)
    statements = ExpertsStatement.objects.filter(expert_id=biegly_id)   
    context = {'profile' : profile, 'statements': statements}   
    return render(request, 'users/a_biegly.html', context)

class OcrView(FormView):
    form_class = UploadForm
    template_name = 'users/ocr.html'
    success_url = '/'

    #def form_valid(self, form):
    #    upload = self.request.FILES['file']
    #    print(type(pytesseract.image_to_string(Image.open(upload))))
    #    return super().form_valid(form)

@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        response_data = {}
        upload = request.FILES['file']
        content = pytesseract.image_to_string(Image.open(upload), lang='pol+eng', config=tessdata_dir_config)
        response_data['content'] = content

        return JsonResponse(response_data)

#@csrf_exempt
#def process_image(request):
#    if request.method == 'POST':
#        response_data = {}
#        upload = request.FILES['file']
#        content = pytesseract.image_to_string(Image.open(upload))
#        print(content)
#        buffer = BytesIO()
#        c = canvas.Canvas(buffer)
#        c.drawString(100, 100, content)
#        c.save()
#        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
#        response['Content-Disposition'] = 'attachment; filename=hello.pdf'        
#        return response
