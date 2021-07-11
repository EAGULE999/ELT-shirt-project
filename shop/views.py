from .models import Category, Subcategory, Product
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout  # add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import requests


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


def store(request):
    context = {}
    return render(request, 'shop/store.html', context)


def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)





def get_weather(request):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    city = "Riga"
    api_key = "8d57e070b401c3295a7f0fc3f2c6836f"

    res = requests.get(url.format(city)).json()
    print(res)


    city_info = {
        'city': city,
        'temp': res.get('main', {}).get('temp'),
        'icon': res.get('weather', {})[0].get('icon'),
        'description': res.get('weather', {})[0].get('description')
        # 'humidity': res.get('main', {}).get('humidity'),
        # 'wind': res.get('wind', {}).get('speed'),
    }

    context = {'city_info': city_info}
    return render(request, 'shop/home.html', context)
