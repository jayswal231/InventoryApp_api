from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class Product_category_viewset(viewsets.ModelViewSet):
    queryset = Product_category.objects.all()
    serializer_class = Product_category_serializer

class Product_viewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_serializer