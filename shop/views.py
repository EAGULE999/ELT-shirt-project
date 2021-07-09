from .models import Category, Subcategory, Product, Mainimage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def main_images(request):
    mainimages = Mainimage.objects.all()
    return render(request, 'shop/home.html', {'mainimages': mainimages})


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


def subcategory_list(request, subcategory_slug=None):
    subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
    products = Product.objects.filter(subcategory=subcategory)
    return render(request, 'shop/products/category.html', {'subcategory': subcategory, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'shop/products/detail.html', {'product': product})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render(request=request, template_name="shop/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="shop/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/")

