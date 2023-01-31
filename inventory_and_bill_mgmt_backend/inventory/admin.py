from django.contrib import admin
from .models import *
# Register your models here.
model = [ Product, Product_category]
for x in model:
    admin.site.register(x)
    