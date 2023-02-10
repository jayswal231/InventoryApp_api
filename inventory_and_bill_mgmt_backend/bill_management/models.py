from django.db import models
from user_accounts.models import CustomUser
# Create your models here.

class TransactionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    particular = models.CharField(max_length=50)
    amount = models.FloatField()

    def __str__(self):
        return self.particular


class BillData(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bill_No = models.CharField(max_length=50,null=True)
    date = models.DateField()
    particulars = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    transaction_amount = models.FloatField()
    transaction_category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.bill_No




