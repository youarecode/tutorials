from django.shortcuts import redirect
from .cart import Cart
from store_app.models import Product
# Create your views here.


def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product)
    return redirect('Store')

def delete_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product)
    return redirect('Store')

def decrease_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.decrease_product(product)
    return redirect('Store')

def clean_cart(request, product_id):
    cart = Cart(request)
    cart.clean_cart()
    return redirect('Store')