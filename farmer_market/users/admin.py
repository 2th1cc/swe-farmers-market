from django.contrib import admin
from django.core.mail import send_mail
from .models import Farmer, Buyer, CustomUser
from orders.models import DeliveryMethod
#Admin works just fine!!
admin.site.register(DeliveryMethod)

@admin.action(description="Enable selected users")
def enable_users(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Disable selected users")
def disable_users(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_active', 'user_type')  # Show relevant fields in the admin list
    list_filter = ('is_active', 'user_type')  # Allow filtering by status and user type
    search_fields = ('email', 'username')  # Allow searching by email or username
    actions = [enable_users, disable_users]  # Add enable/disable actions


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address', 'registration_date', 'default_delivery_method')
    search_fields = ('user__email', 'user__username', 'phone', 'address')
    list_filter = ('registration_date', 'default_delivery_method')

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    # Display the farmer's information including registration details
    list_display = ('user', 'phone', 'farm_name', 'farm_location', 'farm_size', 'registration_date', 'is_approved')
    list_filter = ('is_approved', 'registration_date')
    search_fields = ('user__email', 'phone')
    actions = ['approve_selected_farmers', 'reject_selected_farmers']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_approved=False)
    
    def approve_selected_farmers(self, request, queryset):
        pending_farmers = queryset.filter(is_approved=False)
        for farmer in pending_farmers:
            farmer.approve_feedback = "Your application has been approved!"
            farmer.is_approved = True
            farmer.save()
            self._send_approval_email(farmer)
        self.message_user(request, "Selected pending farmers have been approved and notified.")

    def reject_selected_farmers(self, request, queryset):
        pending_farmers = queryset.filter(is_approved=False)
        for farmer in pending_farmers:
            if not farmer.rejection_feedback:
                farmer.rejection_feedback = "Your application has been reviewed but not approved at this time."
            farmer.is_approved = False
            farmer.save()
            self._send_rejection_email(farmer)
        self.message_user(request, "Selected pending farmers have been rejected and notified with feedback.")

    def _send_approval_email(self, farmer):
        send_mail(
            subject='Your Farmer Account Has Been Approved!',
            message='Congratulations! Your farmer account has been approved. You can now access product listing features.',
            from_email='admin@example.com',
            recipient_list=[farmer.user.email],
            fail_silently=False,
        )

    def _send_rejection_email(self, farmer):
        send_mail(
            subject='Your Farmer Account Application',
            message=f"Unfortunately, your application has not been approved at this time. Reason: {farmer.rejection_feedback}",
            from_email='admin@example.com',
            recipient_list=[farmer.user.email],
            fail_silently=False,
        )

    # Set the description for the custom action in the admin dropdown
    approve_selected_farmers.short_description = "Approve selected pending farmers"
    reject_selected_farmers.short_description = "Reject selected pending farmers with feedback"

    def save_model(self, request, obj, form, change):
    # Check if the approval status was changed
        if change:
            if 'is_approved' in form.changed_data:
                if obj.is_approved:
                    obj.approve_feedback = "Your application has been approved!"
                    self._send_approval_email(obj)
                else:
                    if not obj.rejection_feedback:
                        obj.rejection_feedback = "Your application has been reviewed but not approved at this time."
                    self._send_rejection_email(obj)
        super().save_model(request, obj, form, change)
