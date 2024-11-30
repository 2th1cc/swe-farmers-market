from rest_framework.permissions import BasePermission
from users.models import Farmer 

class IsApprovedFarmer(BasePermission):
    """
    Custom permission class to check if the user is an approved farmer.
    """
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Try to access the Farmer profile via the OneToOne relationship
            try:
                farmer_profile = request.user.farmer_profile
                # Return True if the farmer is approved
                return farmer_profile.is_approved
            except Farmer.DoesNotExist:
                return False
        return False
