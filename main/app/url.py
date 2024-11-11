from django.urls import path
from .views import *

urlpatterns = [
    path('products', productList),
    path('product', addProduct),
    path('product/<int:pk>', detailProduct),
    path('productGroups', productGroupList),
    path('productGroup', addProductGroup),
    path('productGroup/<int:pk>', detailProductGroup),
    path('warehouses', warehouseList),
    path('warehouse', addWarehouse),
    path('warehouse/<int:pk>', detailWarehouse),
]
