from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse("Contacts page!")


def products(request):
    context = {
        "products": products_list,
        "name" : "Daniil"
        }
    return render(request, "victoria/products.html", context)


def products_detail(request, id):
    for prod in products_list:
        if prod["id"] == id:
            return HttpResponse(
                f"Ваш товар номер: {prod["id"]} - {prod["title"]} - {prod["description"]} - {prod["price"]}Kc"
            )
    return HttpResponse(f"Товар не найден!")
