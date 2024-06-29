from django.shortcuts import render
from .models import Product
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/catalog.html', {'products': products})
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/details.html', {'product': product})
