from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def index(request):
    items= Shop.objects.all()
    return render(request, 'shop/index.html', {'items':items})


def help(request):
    return HttpResponse("Help is here")
