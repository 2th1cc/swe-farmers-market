
from rest_framework import serializers
from .models import Buyer, Farmer, CustomUser, Crop
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class ImportantTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["email"] = user.email
        token['user_type'] = user.user_type

        print(f"User being serialized: {user}")

        # Dynamically check for user_type
        if hasattr(user, 'user_type'):
            token['user_type'] = user.user_type
        else:
            token['user_type'] = 'unknown'  # Or handle this gracefully


        return token
# Serializer for handling User data
class UserSerializer(serializers.ModelSerializer):
    # Meta class contains configuration for the UserSerializer
    class Meta:
        model = CustomUser  # Specify the CustomUser model for serialization
        fields = [
                'username',
                'email', 
                'password',
                'phone_number',
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
            phone_number=validated_data.get('phone_number', ''),
            user_type=validated_data.get('user_type')  # Expect user_type in the request
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.is_active = True  # Activate the user by default
        user.save()
        return user
    
# Serializer for handling Farmer data
class FarmerSerializer(serializers.ModelSerializer):
    # Meta class contains configuration for the FarmerSerializer
    crops_grown = serializers.SlugRelatedField(
        many=True,
        queryset=Crop.objects.all(),
        slug_field='name'  # Use the crop name as the field for selection
    )

    class Meta:
        model = Farmer  # Specify the Farmer model for serialization
        fields = [
            'user', 
            'registration_date', 
            'is_approved', 
            'rejection_feedback', 
            'farm_name', 
            'farm_location', 
            'farm_size',
            'soil_type',
            'farm_description', 
            'crops_grown'
        ]

# Serializer for handling Buyer data
class BuyerSerializer(serializers.ModelSerializer):
    # Meta class contains configuration for the BuyerSerializer
    class Meta:
        model = Buyer  # Specify the Buyer model for serialization
        fields = ['user', 
                'registration_date',
                'address',
                'preferred_payment_method',
                'default_delivery_method'
                ]
        # Include fields related to buyer profile information and preferences
