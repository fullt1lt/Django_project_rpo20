from django.urls import path
from victoria.views import home, contacts, products_detail, products, create_product

urlpatterns = [
    path("", home, name="home_page"),
    path("contacts/", contacts, name="contacts_page"),
    path("products/", products, name="products"),
    path("products/<int:id>", products_detail, name="products_detail"),
    path("create-product/", create_product, name="create_product")
]
