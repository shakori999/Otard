from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.ProductAttribute)
admin.site.register(models.ProductAttributeValues)
admin.site.register(models.ProductAttributeValue)
admin.site.register(models.ProductType)
admin.site.register(models.ProductTypeAttribute)
admin.site.register(models.Brand)
admin.site.register(models.Stock)


class InventoryAdmin(admin.ModelAdmin):
    list_display = ("product", "store_price")


admin.site.register(models.ProductInventory, InventoryAdmin)
