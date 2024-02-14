from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def contact(request:HttpRequest):

    if request.method=='POST':
        my_form = ContactForm(request.POST)
        if my_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')

            # inform:dict = my_form.cleaned_data

            # subject = inform['subject']
            # message = inform['message'] + ' ' + inform['email']
            # email_host = settings.EMAIL_HOST_USER
            # recipient_list = ['leinaxd@gmail.com']

            # send_mail(subject, message, email_host, recipient_list,)
            subject = 'message from django'
            body = f"user named {name} with address {email} writes the following:\n\n{content}"
            from_email = ''
            email_sender = EmailMessage(subject, body,from_email, [settings.EMAIL_HOST_USER],reply_to=[email])
            try:
                email_sender.send()
                return redirect('/contact/?valid')
            except:
                return redirect('/contact/?invalid')
                
    else:
        my_form = ContactForm()
    return render(request, 'contact.html', {'my_form':my_form})