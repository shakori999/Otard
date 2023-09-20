from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from ecommerce.search.views import SearchProductInventory
from ecommerce.order.views import *
from ecommerce.checkout.views import *
from ecommerce.drf.views import (
    CategoryList,
    CategoryDetails,
    OrderDetails,
    OrderViewSet,
    ProductByCategory,
    ProductInventoryByWebId,
    ProductRatingViewSet,
    ProductsList,
    ProductDetails,
    CustomersList,
    CustomersDetails,
    store,
    cart,
    checkout,
    )


router=DefaultRouter()
router.register('producctrating', ProductRatingViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", store, name="home"),
    path("cart", cart, name="cart"),
    path("checkout", checkout, name="checkout"),
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
    #path("api/orders/",OrderList.as_view()),
    path("api/order/details/<str:pk>/",OrderDetails.as_view()),
    path("api/search/<str:query>/", SearchProductInventory.as_view()),

]

urlpatterns += router.urls
