from django.urls import path
from shop.views import *

urlpatterns = [
    path('category/create/', CategoryCreateAPI.as_view(), name='category-create'),
    path('category/read/', CategoryListAPI.as_view(), name='category-read'),
    path('category/update/', CategoryUpdateAPI.as_view(), name='category-update'),
    path('category/delete/', CategoryDeleteAPI.as_view(), name='category-delete'),
    path('product/create/', ProductCreateAPI.as_view(), name='product-create'),
    path('product/read/', ProductReadAPI.as_view(), name='product-read'),
    path('product/update/', ProductUpdateAPI.as_view(), name='product-update'),
    path('product/delete/', ProductDeleteAPI.as_view(), name='product-delete'),
]
