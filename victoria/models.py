from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    isStock = models.BooleanField(default=True)
    image = models.ImageField(blank=True, null=True, upload_to="products")
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.quantity} шт - {self.price} Kc"
