from django.shortcuts import render
from .models import *
# Create your views here.

def homeFun(request):
    products = Product.objects.all()
    testimonials = Testimonial.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'testimonials': testimonials, 'categories': categories}
    return render(request, 'home.html', context)

def productsFun(request):
    products = Product.objects.all().order_by('-product_id')
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'products.html', context)

def categoryFun(request, id):
    categories = Category.objects.all()
    categoryDetail = Category.objects.get(pk=id)
    product_category = Product.objects.filter(product_category=categoryDetail)
    context = {'categories': categories, 'categoryDetail': categoryDetail, 'product_category':product_category}
    return render(request, 'category_products.html', context)

def chairFun(request, id):
    productInfo = Product.objects.get(product_id = id)
    categories = Category.objects.all()
    context = {'productInfo': productInfo, 'categories': categories}
    return render(request, 'product.html', context)

def contactFun(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    if request.method == "POST":
        inputName = request.POST['Fname']
        inputSurname = request.POST['Sname']
        inputEmail = request.POST['email']
        inputSMS = request.POST['sms']

        Cotact(contact_name=inputName, contact_surname=inputSurname, contact_email=inputEmail, contact_comment=inputSMS).save()
    return render(request, 'contact.html', context)