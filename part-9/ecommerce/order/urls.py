from django.urls import path
from .views import *

urlpatterns = [
    path('add-to-cart/<uuid:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<uuid:pk>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<uuid:pk>/', remove_single_item_from_cart, name='remove-item-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('ordered-view/', OrderedView.as_view(), name='orderd_view'),
    path('ordered-detail/<uuid:pk>', OrderedDetailView.as_view(), name='order_detail'),
]
