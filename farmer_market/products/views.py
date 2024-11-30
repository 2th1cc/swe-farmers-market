from rest_framework import generics, permissions, filters
from django.shortcuts import get_object_or_404
from .models import Product, ProductImage, LowStockNotification
from .serializers import ProductSerializer, ProductImageSerializer, LowStockNotificationSerializer
from .permissions import IsApprovedFarmer
import logging
from django.shortcuts import render, redirect
from .models import LowStockNotification

# Set up a logger
logger = logging.getLogger(__name__)

# for filtering and sorting and searching
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(quantity__gt=0)  # Only show available products
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category__name', 'farmer__location']  # Search by name, category, and location
    ordering_fields = ['price', 'created_at']  # Sort by price or creation date
#create products
class FarmerProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsApprovedFarmer]

    def get_queryset(self):
        return Product.objects.filter(farmer__user=self.request.user)

    def perform_create(self, serializer):
        farmer_profile = self.request.user.farmerprofile
        product = serializer.save(farmer=farmer_profile)
        logger.info(f"Product {product.name} created by farmer {farmer_profile.farm_name}")

class FarmerProductImageCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsApprovedFarmer]

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id, farmer__user=self.request.user)
        serializer.save(product=product)

class LowStockNotificationListAPIView(generics.ListAPIView):
    serializer_class = LowStockNotificationSerializer
    permission_classes = [permissions.IsAuthenticated, IsApprovedFarmer]

    def get_queryset(self):
        return LowStockNotification.objects.filter(farmer=self.request.user, is_read=False)
