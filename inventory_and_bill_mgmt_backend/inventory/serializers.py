from .models import *
from rest_framework import serializers
import json


class Product_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_category
        fields = '__all__'

class Product_serializer(serializers.ModelSerializer):
    product_category = Product_category_serializer()
 
    def create(self, validated_data):
        print(validated_data)
        category = validated_data.pop("product_category")
        category_data = json.loads(json.dumps(category))

        category_obj = Product_category.objects.create(**category_data)
        product=Product.objects.create(**validated_data, product_category = category_obj )
        return product
        


    class Meta:
        model = Product
        fields = ["particular_name","quantity", "rate", "value", "product_category"]
