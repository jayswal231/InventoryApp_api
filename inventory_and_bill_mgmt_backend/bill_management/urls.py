from django.urls import path,include
from . import views

from Inventory_management.urls import router


router.register('transaction-category', views.TransactionCategory_Viewset, basename='transaction-category')
router.register('bill-data', views.BillData_Viewset, basename='bill-data')
router.register('month-summary', views.MonthlySummary_Viewset, basename='month-summary')

urlpatterns = [
    path('api/', include(router.urls)),
]