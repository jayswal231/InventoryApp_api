from .models import *
from rest_framework import serializers
import json


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_category = ProductCategorySerializer()
 
    def create(self, validated_data):
        current_user = self.context.get('request').user
        category = validated_data.pop("product_category")
        category_data = json.loads(json.dumps(category))

        category_obj = ProductCategory.objects.create(**category_data)
        product=Product.objects.create(**validated_data, product_category = category_obj, user= current_user )
        return product
        
    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['current_user']=self.context['request'].user.username
        return data



    class Meta:
        model = Product
        fields = ["particular_name","quantity", "rate", "value", "product_category"]
