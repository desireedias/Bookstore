from django.db import models

from product.models.category import Category
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=False)

    def __str__(self):
        return self.title
