from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Категории"

class Reviews(models.Model):
    text = models.TextField()
    authors = models.CharField(max_length=20)
    rating = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    is_published = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text[:10]} - {self.rating}"

    class Meta:
        verbose_name_plural = "Отзывы"


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    isStock = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True, upload_to="products")
    category_id = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True, related_name="category"
    )
    review_id = models.ForeignKey(
        Reviews,
        on_delete=models.CASCADE,
        related_name="review",
        blank=True,
        null=True,
    )
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.quantity} шт - {self.price} Kc"
