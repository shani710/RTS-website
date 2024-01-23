from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'homepage.html')

def base_home(request):
    return render(request, 'base_home.html')

def vc_login(request):
    return render(request, 'vc_login.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_log(request):
    return render(request, 'admin_log.html')

def vc(request):
    return render(request, 'vc.html')

def sign_up(request):
    error = ""
    if request.method == "POST":
        name = request.POST.get('firstname')
        contact = request.POST.get('contact')
        pwd = request.POST.get('pwd')
        
        # Get the selected value from the dropdown list
        contact_type = request.POST.get('contact_type')

        try:
            user = User.objects.create_user(first_name=name, password=pwd)
            
            # Use the selected value from the dropdown list
            if contact_type == 'vc':
                VC_Hawks.objects.create(user=user, contact=contact, is_vc=True)
            elif contact_type == 'uc':
                VC_Hawks.objects.create(user=user, contact=contact, is_vc=False)

            error = 'no'
        except:
            error = 'yes'

    return render(request, 'sign_up.html' )

