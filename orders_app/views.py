from django.http import HttpRequest
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderLine
from cart_app.cart import Cart
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.


@login_required(login_url='/authentication/login')
def process_order(request:HttpRequest):
    order = Order.objects.create(user=request.user)
    cart = Cart(request)
    order_line = [
        OrderLine(
            product_id  = key,
            quantity    = value['quantity'],
            user        = request.user,
            order       = order) 
            for key, value in cart.cart.items()]
    
    OrderLine.objects.bulk_create(order_line)
    messages.success(request, 'The order was created successfully')

    send_custom_mail(order=order, 
                     order_line=order_line, 
                     username=request.user.username,
                     usermail=request.user.email)
    cart.clean_cart()
    return redirect('Store')

def send_custom_mail(order, order_line, username, usermail):
    subject = "Thank you for your purchasing order"
    message = render_to_string('order.html',
                               {'order':order,
                                'order_line':order_line,
                                'username':username,
                                'usermail':usermail
                                })
    body = strip_tags(message)
    from_email = settings.EMAIL_HOST_USER
    to = [usermail]

    send_mail(subject, body, from_email, to, html_message=message )