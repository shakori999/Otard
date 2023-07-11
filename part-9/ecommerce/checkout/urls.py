from django.urls import path
from .views import *

urlpatterns = [
    path('', CheckoutPageView.as_view(), name='checkout'),
]