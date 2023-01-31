from django.urls import path,include
from . import views

from Inventory_management.urls import router

router.register('product-category', views.Product_category_viewset, basename='product-category')
router.register('product', views.Product_viewset, basename='product')

urlpatterns = [
    path('api/', include(router.urls)),
]