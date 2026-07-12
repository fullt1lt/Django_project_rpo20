from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import MyForm, CreateProductForm

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

# Create your views here.
def home(request):
    return render(request, "victoria/home.html")

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


def products(request):

    products = Product.objects.filter(price__lte=50000)
    context = {"products": products, "name": "Daniil"}
    return render(request, "victoria/products.html", context)


def products_detail(request, id):
    for prod in products_list:
        if prod["id"] == id:
            return HttpResponse(
                f"Ваш товар номер: {prod["id"]} - {prod["title"]} - {prod["description"]} - {prod["price"]}Kc"
            )
    return HttpResponse(f"Товар не найден!")


def create_product(request):
    form = CreateProductForm()
    if request.method == "POST":
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CreateProductForm()
    return render(request, "victoria/create_product.html", {"form": form})
