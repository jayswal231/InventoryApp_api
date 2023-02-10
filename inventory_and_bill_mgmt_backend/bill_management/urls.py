from django.urls import path,include
from . import views

from Inventory_management.urls import router


router.register('transaction-category', views.TransactionCategoryViewset, basename='transaction-category')
router.register('transaction-type', views.TransactionTypeViewset, basename='transaction-type')
router.register('transaction', views.TransactionViewset, basename='transaction')
router.register('bill-data', views.BillDataViewset, basename='bill-data')
router.register('transaction-summary', views.TransactionSummaryViewset, basename='transaction-summary')
router.register('transaction-summary/<int:year>/<int:year>/', views.TransactionSummaryViewset, basename='transaction-summary')


urlpatterns = [
    path('api/', include(router.urls)),
]