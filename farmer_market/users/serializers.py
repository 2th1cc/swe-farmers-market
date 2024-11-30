from rest_framework import serializers
from .models import Buyer, Farmer, CustomUser
from django.contrib.auth import authenticate

# Serializer for handling User data
class UserSerializer(serializers.ModelSerializer):
    # Meta class contains configuration for the UserSerializer
    class Meta:
        model = CustomUser  # Specify the CustomUser model for serialization
        fields = [
                'username',
                'email', 
                'password',
                'user_type',
                ]  # Fields to include in the serialization process
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': True},
                        }  # Ensure the password is write-only for security reasons
    
    def create(self, validated_data):
        # Dynamically assign user_type based on input data
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data.get('username', ''),
            user_type=validated_data.get('user_type')  # Expect user_type in the request
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.is_active = True  # Activate the user by default
        user.save()
        return user

#authenticate using email
class EmailAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Replace 'username' with 'email'
    password = serializers.CharField()
    
    def validate(self, attrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')

        # Authenticate using the email field
        print(f"Authenticating user: {email}")
        user = authenticate(username=email, password=password)  # Use email as username
        if not user:
            raise serializers.ValidationError("Unable to log in with provided credentials.")
        attrs['user'] = user
        return attrs
    
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
