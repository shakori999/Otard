from django.contrib import admin
from django.urls import path
from ecommerce.checkout.views import *

from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



from ecommerce.drf.views import (
    CategoryList,
    CategoryDetails,
    OrderDetails,
    OrderList,
    ProductByCategory,
    ProductInventoryByWebId,
    ProductsList,
    ProductDetails,
    CustomersList,
    CustomersDetails,
    
    )
from ecommerce.search.views import SearchProductInventory
from ecommerce.order.views import *





urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/customers/all/", CustomersList.as_view()),
    path("api/customer/detail/<int:pk>/", CustomersDetails.as_view()),
    path("api/inventory/categories/all/", CategoryList.as_view()),
    path("api/inventory/category/<str:pk>/", CategoryDetails.as_view()),
    path("api/inventory/products/category/<str:query>/",ProductByCategory.as_view()),
    path("api/inventory/products/all/", ProductsList.as_view()),
    path("api/inventory/product/<int:pk>/", ProductInventoryByWebId.as_view()),
    path("api/inventory/product/details/<str:pk>/", ProductDetails.as_view()),
    path("api/orders/",OrderList.as_view()),
    path("api/order/details/<str:pk>/",OrderDetails.as_view()),
    path("api/search/<str:query>/", SearchProductInventory.as_view()),

]
