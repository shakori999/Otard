from django.contrib import admin

from ecommerce.inventory.models import *




admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductType)
admin.site.register(ProductTypeAttribute)
admin.site.register(Brand)
admin.site.register(Stock)
admin.site.register(ProductRating)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


admin.site.register(ProductInventory, InventoryAdmin)
