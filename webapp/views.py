from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import datetime
from django.template import Template, Context
from django.template.loader import get_template


from webapp.models import Article

import sys, os
# Create your views here by defining a function

def hello_world(request):
    """First view."""
    test = 6
    ctx = {"time":datetime.datetime.now(), 'themes':['dark','light']} #.pop('themes'))

    if test == 1:
        print('hola',request,'chau')
        doc_1 = '<h1>Hello World! and beyond!</h1>' #Simple text
        return HttpResponse(doc_1)
    if test == 2:
        doc_2 = '''<html><body><h1>Hello World! and beyond!</h1></body></html>''' #same 
        return HttpResponse(doc_2)
    if test == 3:
        doc_3 = f'''<html><body><h2>Date today: {datetime.datetime.now()}</h2></body></html'''
        return HttpResponse(doc_3)
    if test == 4:
        path = os.getcwd() +'/tutorial/templates/hello_world.html'       
        print(path)
        with open(path) as f:
            plt = Template(f.read())
        doc_4 = plt.render(Context(ctx))
        return HttpResponse(doc_4)
    if test == 5:
        # in your settings Define include your templates dir for your templates
        doc_5 = get_template('hello_world.html').render(ctx)
        return HttpResponse(doc_5)
    if test == 6:
        return render(request, 'hello_world.html', ctx)
    

def compute_age(request, age_today, year):
    period  = year - datetime.datetime.now().year
    future_age = age_today + period

    doc = f'''You will have {future_age} at year {year}'''

    return HttpResponse(doc)


def machine_learning(request):
    ctx = {'time':datetime.datetime.now()}
    return render(request, 'machine_learning.html', ctx)

def control_theory(request):
    ctx = {'time':datetime.datetime.now()}
    return render(request, 'control_theory.html', ctx)


# Searching a product
def search_products(request):
    return render(request, 'product_search.html')


def search(request:HttpRequest):
    """test cases:
    - blank input
    - long input
    - valid input
    """
    searched_product = request.GET['product'] #html: input type text
    if len(searched_product) > 20:
        return HttpResponse('searching request too long')
    
    if searched_product:
        msg = f"Searched article: {searched_product}" 
        article = Article.objects.filter(name__icontains=searched_product)
        return render(request, 'search_results.html',{'articles':article, 'query':searched_product})
    else:
        msg = f"you haven't introduced anything" 
    return HttpResponse(msg)



def home(request):
    return render(request, 'home.html')
