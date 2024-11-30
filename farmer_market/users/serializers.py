from rest_framework import serializers
from .models import Buyer, Farmer, CustomUser

# Serializer for handling User data
class UserSerializer(serializers.ModelSerializer):
    # Meta class contains configuration for the UserSerializer
    class Meta:
        model = CustomUser  # Specify the CustomUser model for serialization
        fields = ['username',
                'email', 
                'password'
                ]  # Fields to include in the serialization process
        extra_kwargs = {'password': {'write_only': True}}  # Ensure the password is write-only for security reasons
    
    def create(self, validated_data):
        # Use the custom user manager's create_user method to create a user instance
        # This method handles password hashing and other user creation logic
        return CustomUser.objects.create_user(**validated_data)


# Serializer for handling Farmer data
class FarmerSerializer(serializers.ModelSerializer):
    # Meta class contains configuration for the FarmerSerializer
    class Meta:
        model = Farmer  # Specify the Farmer model for serialization
        fields = [
            'user', 
            'phone', 
            'registration_date', 
            'is_approved', 
            'rejection_feedback', 
            'farm_name', 
            'farm_location', 
            'farm_size',
            'soil_type'
        ]

# Serializer for handling Buyer data
class BuyerSerializer(serializers.ModelSerializer):
    # Meta class contains configuration for the BuyerSerializer
    class Meta:
        model = Buyer  # Specify the Buyer model for serialization
        fields = ['user', 
                'phone', 
                'registration_date',
                'address',
                'default_delivery_method'
                ]
        # Include fields related to buyer profile information and preferences
