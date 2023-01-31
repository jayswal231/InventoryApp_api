from django.contrib import admin
from .models import *
# Register your models here.
model= [TransactionCategory,BillData,MonthlySummary]
admin.site.register(model)