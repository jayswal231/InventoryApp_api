from django.contrib import admin
from .models import *
# Register your models here.
model = [ Product, ProductCategory]
for x in model:
    admin.site.register(x)
    