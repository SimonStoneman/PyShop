from django.db import models

# Create your models here.


class Product(models.Model): # inherit from model
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.FloatField()
    image_url = models.CharField(max_length=2083)


class Discount(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
