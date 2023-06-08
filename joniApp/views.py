from django.shortcuts import render
from .models import Product, Testimonial
# Create your views here.

def homeFun(request):
    products = Product.objects.all()
    testimonials = Testimonial.objects.all()
    context = {'products': products, 'testimonials': testimonials}
    return render(request, 'home.html', context)

def productsFun(request):
    products = Product.objects.all().order_by('-product_id')
    context = {'products': products}
    return render(request, 'products.html', context)

def categoryFun(request):
    return render(request, 'category_products.html')

def chairFun(request, id):
    productInfo = Product.objects.get(product_id = id)
    context = {'productInfo': productInfo}
    return render(request, 'product.html', context)

def contactFun(request):
    return render(request, 'contact.html')