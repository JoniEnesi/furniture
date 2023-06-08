from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeFun, name="home"),
    path('products/', views.productsFun, name="products"),
    path('category_products/', views.categoryFun, name="category"),
    path('product/<id>/', views.chairFun, name="product"),
    path('contact/', views.contactFun, name="contact")
]