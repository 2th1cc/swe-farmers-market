from django.contrib import admin
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from .views import (
    FarmerDashboardAPIView,
    BuyerDashboardAPIView,
    LoginAPIView,
    FarmerRegistrationAPIView,
    BuyerRegistrationAPIView,

    AdminBuyerListView,
    AdminFarmerListView,
    AdminEditUserView,
    AdminDeleteUserView,
    AdminToggleUserStatusView,
)

urlpatterns = [
    # Authentication and Registration for mobile app users
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/register/farmer/', FarmerRegistrationAPIView.as_view(), name='farmer_register_api'),
    path('api/register/buyer/', BuyerRegistrationAPIView.as_view(), name='buyer_register_api'),
    
    # API Dashboards for mobile application access
    path('api/dashboard/farmer/', FarmerDashboardAPIView.as_view(), name='farmer_dashboard_api'),
    path('api/dashboard/buyer/', BuyerDashboardAPIView.as_view(), name='buyer_dashboard_api'),

    path('', lambda request: redirect('login')),
    path('admin/buyers/', AdminBuyerListView.as_view(), name='admin_buyer_list'),  # View all buyers
    path('admin/buyers/<int:buyer_id>/', AdminBuyerListView.as_view(), name='admin_buyer_detail'),  # View specific buyer
    path('admin/farmers/', AdminFarmerListView.as_view(), name='admin_farmer_list'),  # View all farmers
    path('admin/farmers/<int:farmer_id>/', AdminFarmerListView.as_view(), name='admin_farmer_detail'),  # View specific farmer
    path('admin/users/<int:user_id>/edit/', AdminEditUserView.as_view(), name='admin_edit_user'),  # Edit user
    path('admin/users/<int:user_id>/delete/', AdminDeleteUserView.as_view(), name='admin_delete_user'),  # Delete user
    path('admin/users/<int:user_id>/toggle-status/', AdminToggleUserStatusView.as_view(), name='admin_toggle_user_status'),  # Enable/Disable user
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('admin/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('admin/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('admin/password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]