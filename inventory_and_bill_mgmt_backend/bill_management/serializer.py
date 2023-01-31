from .models import *
from rest_framework import serializers


class TransactionCategory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = '__all__'

class BillData_Serializer(serializers.ModelSerializer):
    class Meta:
        model = BillData
        fields = '__all__'

class MonthlySummary_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlySummary
        fields = '__all__'