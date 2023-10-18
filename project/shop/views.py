from django.shortcuts import render, HttpResponse, redirect
from .models import *
from carts.forms import CartAddProductForm


# Create your views here.

def index(request):
    items = Shop.objects.all()
    return render(request, 'shop/index.html', {'items': items})


def help(request):
    return HttpResponse("Help is here")


def detail(request, item_id):
    try:
        item: object = Shop.objects.get(id=item_id)
        cart_product_form = CartAddProductForm()
    except:
        return redirect(index, permanent=True)

    return render(request, 'shop/detail.html', {'item': item, 'cart_product_form': cart_product_form})
