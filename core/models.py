from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    value_defalt = models.DecimalField(decimal_places=2, max_digits=10)
    tags = models.ManyToManyField(Tag)
    categories = models.ManyToManyField(Category)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.name
