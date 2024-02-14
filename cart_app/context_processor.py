"""
A context processor is a variable living outside the place it was created.
in other words, it's a globar variable

remember to include this into the template at settings.py
"""
from django.http import HttpRequest

def total_amount(request:HttpRequest):
    total = 0

    if request.user.is_authenticated and 'cart' in request.session:
        for key,value in request.session['cart'].items():
            total += float(value['price'])

    return {'cart_total_amount':total}