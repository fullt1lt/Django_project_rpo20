from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .forms import MyForm, CreateProductForm, LoginForm

from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test

products_list = [
    {
        "id": 1,
        "title": "Телефон",
        "description": "Смартфон с хорошей камерой",
        "price": 35000,
        "is_stock" : True,
    },
    {
        "id": 2,
        "title": "Планшет",
        "description": "Планшет для работы и учёбы",
        "price": 20000,
        "is_stock" : True
    },
    {
        "id": 3,
        "title": "Ноутбук",
        "description": "Мощный ноутбук для программирования",
        "price": 70000,
        "is_stock" : False
    },
    {
        "id": 4,
        "title": "Монитор",
        "description": "Монитор с диагональю 27 дюймов",
        "price": 15000,
        "is_stock" : True
    },
    {
        "id": 5,
        "title": "Мышка",
        "description": "Беспроводная компьютерная мышка",
        "price": 1500,
        "is_stock" : False
    }
]


class HomePage(TemplateView):
    template_name = "victoria/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["title"] = "Супер пупер продукты"
        return context


def contacts(request):
    my_form = MyForm()
    if request.method == "POST":
        my_form = MyForm(request.POST)
        if my_form.is_valid():
            email = my_form.cleaned_data["email"]
            password = my_form.cleaned_data["password"]
            return render(
                request,
                "victoria/contacts.html",
                {"email": email, "password": password, "form": my_form}
            )
    return render(request, "victoria/contacts.html", {"form": my_form})


def is_staff(user):
    return user.is_superuser


@login_required
@user_passes_test(is_staff)
def products(request):

    products = Product.objects.all()
    context = {"products": products, "name": "Daniil"}
    return render(request, "victoria/products.html", context)


def products_detail(request, id):
    for prod in products_list:
        if prod["id"] == id:
            return HttpResponse(
                f"Ваш товар номер: {prod["id"]} - {prod["title"]} - {prod["description"]} - {prod["price"]}Kc"
            )
    return HttpResponse(f"Товар не найден!")


class CreateProduct(View):
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        form = CreateProductForm()
        return render(request, "victoria/create_product.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CreateProductForm()
        return render(request, "victoria/create_product.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
        return render(request, "victoria/register.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "victoria/register.html", {"form" : form})


def my_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect("home_page")
        return render(request, "victoria/login.html", {"form": form})
    else:
        form = LoginForm
        return render(request, "victoria/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home_page")
