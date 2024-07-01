from django.shortcuts import render
from .models import Product, product_images
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/catalog.html', {'products': products})
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    product_image = product_images.objects.filter(product = product)
    return render(request, 'products/details.html', {'product': product, 'product_images': product_image})
