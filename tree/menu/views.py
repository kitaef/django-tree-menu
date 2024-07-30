from django.shortcuts import render
from menu.models import Menu


# Create your views here.

def index(request):
    return render(request, 'menu/index.html')

def menu(request, menu_url):
    return render(request, 'menu/index.html', {'menu_url': menu_url})