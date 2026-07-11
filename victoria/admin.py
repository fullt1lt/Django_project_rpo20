from django.contrib import admin
from .models import Product, Category, Reviews
# Register your models here.

class CustomProduct(admin.ModelAdmin):
    list_display = ["title", "price", "isStock", "quantity"]
    search_fields = ("title",)
    list_filter = ("price",)
    fieldsets = (
        (
            "Основная информация:",
            {"fields": ("title", "description", "image", "category_id", "review_id")},
        ),
        ("Бюрократия:", {"fields": ("price", "quantity", "isStock")}),
        ("Даты:", {"fields": ("create_at", "update_at")}),
    )

    readonly_fields = ("create_at", "update_at")


class CustomCategory(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ("title",)


class CustomReviews(admin.ModelAdmin):
    list_display = ["authors", "rating", "is_published", "create_at"]
    list_filter = ("create_at", "is_published")


admin.site.register(Product, CustomProduct)
admin.site.register(Category, CustomCategory)
admin.site.register(Reviews, CustomReviews)
