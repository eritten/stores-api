from django.db import models

# Create your models here.


class Category(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Store(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='stores')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    stores = models.ManyToManyField(Store, related_name='products')

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')
