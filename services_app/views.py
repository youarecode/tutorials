from django.shortcuts import render

from .models import Service
# Create your views here.

def services(request):
    s = Service.objects.all()
    return render(request, 'services.html', {'services':s})


