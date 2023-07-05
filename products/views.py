from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

# /product ->


def index(request):
    products = Product.objects.all()
    return render(request, # the html page request
                  'index.html', # the name of the html template
                  {'products': products}) # the dictionary containing our items


def new(request):
    return HttpResponse('New product page')

