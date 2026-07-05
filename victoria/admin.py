from django.contrib import admin
from .models import Product
# Register your models here.

class CustomProduct(admin.ModelAdmin):
    list_display = ["title", "price", "isStock", "quantity"]
    search_fields = ("title",)
    list_filter = ("price",)
    fieldsets = (
        ("Основная информация:", {"fields": ("title", "description", "image")}),
        ("Бюрократия:", {"fields": ("price", "quantity", "isStock")}),
        ("Даты:", {"fields": ("create_at", "update_at")}),
    )

    readonly_fields = ("create_at", "update_at")


admin.site.register(Product, CustomProduct)
