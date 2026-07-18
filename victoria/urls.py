from django.urls import path
from victoria.views import HomePage, contacts, products_detail, products, CreateProduct, register, my_login, logout_view

urlpatterns = [
    path("", HomePage.as_view(), name="home_page"),
    path("contacts/", contacts, name="contacts_page"),
    path("products/", products, name="products"),
    path("products/<int:id>", products_detail, name="products_detail"),
    path("create-product/", CreateProduct.as_view(), name="create_product"),
    path("register/", register, name="register"),
    path("login/", my_login, name="login"),
    path("logout/", logout_view, name="logout"),
]
