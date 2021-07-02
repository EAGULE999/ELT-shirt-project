from django.shortcuts import render
from .models import Category, Subcategory, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def subcategories(request):
    return {
        'subcategories': Subcategory.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})
