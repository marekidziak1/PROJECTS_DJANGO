from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def home(request):
    context={}
    return render(request, 'accounts/dashboard.html', context)
def contact(request):
    context={}
    return render(request, 'accounts/contact.html', context)
def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'accounts/products.html', context)
def customer(request):
    context={}
    return render(request, 'accounts/customer.html', context)
# Create your views here.
