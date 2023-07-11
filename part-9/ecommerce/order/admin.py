from django.contrib import admin
from .models import *
# Register your models here.

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user','ordered_date',)

admin.site.register(OrderItem)
admin.site.register(Order, OrderItemAdmin)