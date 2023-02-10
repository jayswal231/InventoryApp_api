from django.contrib import admin
from .models import *
# Register your models here.
model= [TransactionCategory, TransactionType, BillData,Transaction]
admin.site.register(model)