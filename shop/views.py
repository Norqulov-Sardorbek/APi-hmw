from rest_framework import generics

from shop.models import Category, Product
from shop.serializer import CategorySerializer, ProductSerializer


# Create your views here.


class CategoryCreateAPI(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateAPI(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteAPI(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCreateAPI(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductReadAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteAPI(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
