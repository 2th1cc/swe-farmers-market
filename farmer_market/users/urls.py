from django.contrib import admin
from django.urls import path
from .views import (
    FarmerDashboardAPIView,
    BuyerDashboardAPIView,
    LoginAPIView,
    FarmerRegistrationAPIView,
    BuyerRegistrationAPIView,
)

urlpatterns = [

    # Authentication and Registration for mobile app users
    path('api/login/', LoginAPIView.as_view(), name='login_api'),
    path('api/register/farmer/', FarmerRegistrationAPIView.as_view(), name='farmer_register_api'),
    path('api/register/buyer/', BuyerRegistrationAPIView.as_view(), name='buyer_register_api'),

    # API Dashboards for mobile application access
    path('api/dashboard/farmer/', FarmerDashboardAPIView.as_view(), name='farmer_dashboard_api'),
    path('api/dashboard/buyer/', BuyerDashboardAPIView.as_view(), name='buyer_dashboard_api'),
]