from django.urls import path,include
from . import views

from Inventory_management.urls import router

router.register('product-category', views.ProductCategoryViewset, basename='product-category')
router.register('product', views.ProductViewset, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]