from django.shortcuts import render
from django.http import HttpResponse

products_list = [
    {
        "id": 1,
        "title": "Телефон",
        "description": "Смартфон с хорошей камерой",
        "price": 35000,
    },
    {
        "id": 2,
        "title": "Планшет",
        "description": "Планшет для работы и учёбы",
        "price": 20000,
    },
    {
        "id": 3,
        "title": "Ноутбук",
        "description": "Мощный ноутбук для программирования",
        "price": 70000,
    },
    {
        "id": 4,
        "title": "Монитор",
        "description": "Монитор с диагональю 27 дюймов",
        "price": 15000,
    },
    {
        "id": 5,
        "title": "Мышка",
        "description": "Беспроводная компьютерная мышка",
        "price": 1500,
    },
]

# Create your views here.
def home(request):
    return HttpResponse("Hello it is home page!")

def contacts(request):
    return HttpResponse("Contacts page!")


def products(request):
    text = f"<h1 style='color: red;'>Ваш товар номер: <br></h1>" 
    for prod in products_list:
        text += f"{prod["id"]} - {prod["title"]} <br>"
    return HttpResponse(text)


def products_detail(request, id):
    for prod in products_list:
        if prod["id"] == id:
            return HttpResponse(
                f"Ваш товар номер: {prod["id"]} - {prod["title"]} - {prod["description"]} - {prod["price"]}Kc"
            )
    return HttpResponse(f"Товар не найден!")
