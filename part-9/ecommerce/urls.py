from django.contrib import admin
from django.urls import path
from ecommerce.checkout.views import *

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


from ecommerce.drf.views import (
    CategoryList,
    CategoryDetails,
    ProductByCategory,
    ProductInventoryByWebId,
    ProductsList,
    ProductDetails,
    )
from ecommerce.search.views import SearchProductInventory
from ecommerce.order.views import *





urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/inventory/categories/all/", CategoryList.as_view()),
    path("api/inventory/category/<str:pk>/", CategoryDetails.as_view()),
    path("api/inventory/products/category/<str:query>/",ProductByCategory.as_view()),
    path("api/inventory/products/all/", ProductsList.as_view()),
    path("api/inventory/product/<int:query>/", ProductInventoryByWebId.as_view()),
    path("api/inventory/product/<str:pk>/", ProductDetails.as_view()),
    path("api/search/<str:query>/", SearchProductInventory.as_view()),

]
