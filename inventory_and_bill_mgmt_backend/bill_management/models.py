from django.db import models
from user_accounts.models import CustomUser
# Create your models here.

class TransactionCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class BillData(models.Model):
 #   user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    bill_No = models.CharField(max_length=50,null=True)
    date = models.DateField()
    particulars = models.CharField(max_length=100)
    transaction_amount = models.FloatField()
    transaction_category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    transaction_type = (
        ("cash_In","cash_In"),("cash_out","cash_out"),("fonepay","fonepay"),("cheque","cheque")
    )
    transaction_type = models.CharField(max_length=50, choices=transaction_type, default="cash_In")

    def __str__(self):
        return self.bill_No


class MonthlySummary(models.Model):
    month = (
        ("january","january"),   
        ("February","February"), 
        ("March","March"),       
        ("April","April"),       
        ("May","May"),           
        ("June","June"),
        ("July","July"),
        ("August","August"),
        ("September","September"),
        ("October","October"),
        ("November","November"),
        ("December","December")
    )
    month = models.CharField(max_length=50, choices=month)
    transfer_capital = models.FloatField()
    laundary_total = models.FloatField()
    CashIn_total = models.FloatField()
    Cashout_total = models.FloatField()
    Bank_total = models.FloatField()

    def __str__(self) -> str:
        return self.transfer_capital



