from django.db import models
from user_accounts.models import CustomUser
# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    particular_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    rate = models.FloatField()
    value = models.FloatField()
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.particular_name
