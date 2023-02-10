from .models import *
from rest_framework import serializers


class TransactionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = '__all__'

   
       
    

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class BillDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillData
        fields = '__all__'

    

class TransactionSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = BillData
        fields=[]

