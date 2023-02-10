from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import date
from django.db.models import Sum

# Create your views here.

class TransactionCategoryViewset(viewsets.ModelViewSet):
    queryset = TransactionCategory.objects.all()
    serializer_class = TransactionCategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"transaction_category": [item["name"] for item in serializer.data]})
       
class TransactionTypeViewset(viewsets.ModelViewSet):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer

class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class BillDataViewset(viewsets.ModelViewSet):
    queryset = BillData.objects.all()
    serializer_class = BillDataSerializer




import json
class TransactionSummaryViewset(viewsets.ModelViewSet):
    queryset= BillData.objects.all()
    serializer_class= TransactionSummarySerializer
    

    def list(self, request, *args, **kwargs):
        result = {
            "category": {},
            "type": {},
            "date": ''
        }
    
        start_date=self.request.GET.get('start_date')
        end_date=self.request.GET.get('end_date')
        print(start_date)
        print(end_date)
        

        # result["date"] = date
        total=[]
        all_category = TransactionCategory.objects.all()
        for data in all_category:
            current_category_total = self.get_queryset().filter(transaction_category=data, date__range=(start_date,end_date)).aggregate(total=Sum('transaction_amount'))
            
            result["category"].update({
                data.name  + "_total": current_category_total["total"]or 0
            
            })

        
        all_type = TransactionType.objects.all()
        for data in all_type:
            current_type_total = self.get_queryset().filter(transaction_type=data, date__range=(start_date,end_date)).aggregate(total=Sum('transaction_amount'))
            
            result["type"].update({
                data.name  + "_total": current_type_total["total"]or 0
            })
        return Response(result)
    