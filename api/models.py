from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_description = models.TextField()
    

