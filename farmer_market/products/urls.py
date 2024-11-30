from django.urls import path, include
from .views import (
    FarmerProductListCreateAPIView,
    FarmerProductImageCreateAPIView,
    LowStockNotificationListAPIView,
    ProductListAPIView
)

urlpatterns = [
    path('api/farmer/products/', FarmerProductListCreateAPIView.as_view(), name='farmer_product_list_create'),
    path('api/farmer/products/<int:product_id>/images/', FarmerProductImageCreateAPIView.as_view(), name='farmer_product_image_create'),
    path('api/farmer/notifications/low-stock/', LowStockNotificationListAPIView.as_view(), name='low_stock_notifications'),
    path('api/products/', ProductListAPIView.as_view(), name='product_list'),

    path('api/token/', views.obtain_auth_token, name='obtain_auth_token'),
]
