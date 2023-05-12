from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='product', blank=True, null=True)

    def __str__(self):
        return f'{self.name} (stock: {self.stock})'
