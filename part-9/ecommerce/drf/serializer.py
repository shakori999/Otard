from attr import attributes, fields
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from ecommerce import order
from ecommerce.inventory.models import (
    Brand,
    Category,
    Media,
    Product,
    ProductAttributeValue,
    ProductAttributeValues,
    ProductInventory,
    ProductRating,
    ProductType,
    ProductRating,
)
from ecommerce.accounts.models import CustomUser 
from django.contrib.auth.models import User
from ecommerce.order.models import Order, OrderItem
from ecommerce.promotion.models import Promotion
from rest_framework import serializers


class CustomersListSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(max_value=50)
    address = serializers.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ["username","email","phone", "address"]
        read_only = True

    def __init__(self, *args, **kwargs):
        super(CustomersListSerializer, self).__init__(*args, **kwargs)


class CustomersDetialsSerializer(serializers.ModelSerializer):
    phone = serializers.IntegerField(max_value=50)
    address = serializers.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ["username","email","phone", "address"]
        read_only = True

    def __init__(self, *args, **kwargs):
        super(CustomersDetialsSerializer, self).__init__(*args, **kwargs)

class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        depth = 2
        exclude = ["id"]
        read_only = True


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]
        read_only = True


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "is_active"]
        read_only = True
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","name", "web_id"]
        read_only = True
        editable = False
        depth = 1



class ProductMediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return obj.img_url.url


class ProductInventorySerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)
    media = ProductMediaSerializer(many=True, read_only=True)
    brand = BrandSerializer(read_only=True)
    attributes = ProductAttributeValueSerializer(source="attribute_values", many=True, read_only=True)
    promotion_price = serializers.SerializerMethodField()
    product_ratings = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "brand",
            "product",
            "weight",
            "media",
            "attributes",
            "product_type",
            "promotion_price",
            "product_ratings",
            
        ]
        depth=2
        read_only = True


    def get_promotion_price(self, obj):

        try:
            x = Promotion.products_on_promotion.through.objects.get(
                Q(promotion_id__is_active=True) & Q(product_inventory_id=obj.id)
            )
            return x.promo_price
        except ObjectDoesNotExist:
            return None


class ProductInventorySearchSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False, read_only=True)
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            "product",
            "brand",
        ]

class OrderDetailsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(max_length=50)
    sub_total = serializers.SerializerMethodField( method_name="total")

    class Meta:
        model= OrderItem
        fields = [
                "ordered",
                "user",
                "item",
                "quantity",
                "sub_total",
        ]

        
    
    def total(self, cartitem:OrderItem):
        return cartitem.quantity * cartitem.item.store_price

    
    
    


class OrderSerializer(serializers.ModelSerializer):
    #item_name = OrderDetailsSerializer(many=True, read_only=True)
    grand_total = serializers.SerializerMethodField(method_name='main_total')
    item_name = serializers.StringRelatedField(many=False, read_only=True)
    
    class Meta:
        model = Order
        fields = "__all__"
        read_only = True
        depth=1

    def main_total(self, cart: Order):
        items = cart.items.all()
        total = sum([item.quantity * item.item.store_price for item in items])
        return total

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRating
        fields=['id', 'customer', 'product', 'rating', 'reviews','add_time']

    def __init__(self, *args, **kwargs):
        super(ProductRatingSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1




