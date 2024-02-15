from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from .forms import RegisterForm
# Create your views here.


class VRegister(View):
    def get(self, request):
        """manages the rendering"""
        form=RegisterForm()
        return render(request, 'register.html', {'form':form})
    
    def post(self, request):
        """manages the shipment of forms"""
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'register.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect('Home')

def login(request:HttpRequest):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            password  = form.cleaned_data['password']
            user = auth.authenticate(username=user_name, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('Home')
            else: #This error should never happen, is_valid already checks if the user is logged in
                messages.error(request, 'invalid login')
        else:
            messages.error(request, 'Wrong username or password')
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})