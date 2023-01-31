from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class TransactionCategory_Viewset(viewsets.ModelViewSet):
    queryset = TransactionCategory.objects.all()
    serializer_class = TransactionCategory_Serializer


class BillData_Viewset(viewsets.ModelViewSet):
    queryset = BillData.objects.all()
    serializer_class = BillData_Serializer


class MonthlySummary_Viewset(viewsets.ModelViewSet):
    queryset = MonthlySummary.objects.all()
    serializer_class = MonthlySummary_Serializer
