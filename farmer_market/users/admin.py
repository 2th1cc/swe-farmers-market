from django.contrib import admin
from django.core.mail import send_mail
from .models import Farmer

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    # Display the farmer's information including registration details
    list_display = ('user', 'phone', 'farm_name', 'farm_location', 'farm_size', 'registration_date', 'is_approved')
    
    list_filter = ('is_approved', 'registration_date')
    search_fields = ('user__email', 'phone')
    actions = ['approve_selected_farmers', 'reject_selected_farmers']

    def approve_selected_farmers(self, request, queryset):
        pending_farmers = queryset.filter(is_approved=False)
        for farmer in pending_farmers:
            farmer.is_approved = True
            farmer.save()
            self._send_approval_email(farmer)
        self.message_user(request, "Selected pending farmers have been approved and notified.")

    def reject_selected_farmers(self, request, queryset):
        pending_farmers = queryset.filter(is_approved=False)
        for farmer in pending_farmers:
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