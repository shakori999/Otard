from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, generics, permissions, pagination
from rest_framework.response import Response
from rest_framework.views import APIView

from ecommerce.accounts.models import CustomUser
from ecommerce.inventory.models import Category, Product, ProductInventory, ProductRating
from ecommerce.order.models import Order, OrderItem
from ecommerce.drf.serializer import (
    CategorySerializer,
    OrderDetailsSerializer,
    OrderSerializer,
    ProductInventorySerializer,
    ProductRatingSerializer,
    ProductSerializer,
    CustomersListSerializer,
    CustomersDetialsSerializer,
)

class CustomersList(generics.ListCreateAPIView):
    """
    Return list of all Customers
    """
    permission_classes=[permissions.IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomersListSerializer
    
class CustomersDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Return list of all Customers
    """
    #permission_classes=[permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomersDetialsSerializer

    def get(self, request, pk):
        product = get_object_or_404(CustomUser, id=pk)
        serializer = CustomersDetialsSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(CustomUser, id=pk)
        serializer = CustomersDetialsSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        product = get_object_or_404(CustomUser, id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryList(generics.ListAPIView):
    """
    Return list of all categories
    """
    #permission_classes=[permissions.IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

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
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

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




class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetails(generics.ListAPIView):
    """TODO: add admin auth to see all orders details ,and another one for customer's order details only
       this is a simple api for customer's order details view
        def get_queryset(self):
            order_id = self.kwargs['pk']
            order_2 = Order.objects.get(user=self.request.user, ordered=False)
            order_items = OrderItem.objects.filter(order=order_2)
            return order_items
"""
    serializer_class = OrderDetailsSerializer
    def get_queryset(self):
        order_id = self.kwargs['pk']
        order = Order.objects.get(id=order_id)
        order_2 = Order.objects.get(user=self.request.user, ordered=False)
        order_items = OrderItem.objects.filter(order=order)
        return order_items


    
class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ProductRatingSerializer
    queryset = ProductRating.objects.all()
        


        
    
    


