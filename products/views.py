from django.shortcuts import render
from .models import Product
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/index2.html', {'product': product})
from django.http import HttpResponse
def home(request):
    return HttpResponse('Hello, World!')