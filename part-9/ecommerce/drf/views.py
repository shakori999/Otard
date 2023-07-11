from django.shortcuts import render, get_object_or_404
from django.views import generic
from ecommerce.drf.serializer import (
    CategorySerializer,
    ProductInventorySerializer,
    ProductSerializer,
    CartItemSerializer,
    CartSerializer,
)
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import (
        CreateModelMixin,
        RetrieveModelMixin,
        DestroyModelMixin,
        )
from ecommerce.inventory.models import Category, Product, ProductInventory
from ecommerce.order.models import Order, OrderItem

class CategoryList(APIView):
    """
    Return list of all categories
    """
    #permission_classes=[permissions.IsAuthenticated]

    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CategoryDetails(APIView):
    """
    Return a category details
    """
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductsList(generics.ListAPIView):
    """
    Reeturn a list of all products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductByCategory(APIView):
    """
    Return product by category
    """

    def get(self, request, query=None):
        queryset = Product.objects.filter(category__slug=query)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductInventoryByWebId(generics.RetrieveUpdateDestroyAPIView):
    """
    Return Sub Product by WebId
    """

    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

    def get(self, request, pk):
        queryset = ProductInventory.objects.filter(product__web_id=pk)
        serializer = ProductInventorySerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(ProductInventory, product__web_id=pk)
        serializer = ProductInventorySerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        product = get_object_or_404(ProductInventory, product__web_id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









    
        


        
    
    


