from django.shortcuts import render

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

