from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Buyer, Farmer, CustomUser, DeliveryMethod
from .serializers import BuyerSerializer, FarmerSerializer, UserSerializer  # Serializers to convert model data to JSON
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken


# Endpoint for user login using token authentication
class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Use the DRF's built-in serializer for handling login data (username/password)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)  # Validate data and raise an error if invalid
        user = serializer.validated_data['user']  # Retrieve the authenticated user from validated data
        token, created = Token.objects.get_or_create(user=user)  # Get or create an authentication token for the user
        return Response({'token': token.key})  # Return the token to the client


# API view for registering a new farmer
class FarmerRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Deserialize incoming user data using the UserSerializer
        user_serializer = UserSerializer(data=request.data)
        
        # Check if user data is valid
        if user_serializer.is_valid():
            # Create the user with user_type indicating they are a farmer
            user = user_serializer.save(user_type=2)  
            
            # Collect additional farmer-specific fields
            farm_name = request.data.get('farm_name')  # Use empty string as default if missing
            farm_location = request.data.get('farm_location')
            farm_size = request.data.get('farm_size')
            phone = request.data.get('phone')
            
            # Create farmer profile with additional fields
            Farmer.objects.create(
                user=user,
                phone=phone,
                farm_name=farm_name,
                farm_location=farm_location,
                farm_size=farm_size,
                is_approved=False,  # New farmers are not approved by default
                rejection_feedback=''  # Initialize with an empty string
            )
            
            # Send a welcome email for registration
            self._send_registration_email(user)
            
            # Return a success response
            return Response({'message': 'Farmer registered successfully!'}, status=status.HTTP_201_CREATED)
        
        # Return any errors in the data validation process
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _send_registration_email(self, user):
        # Send an email notification for successful registration
        send_mail(
            subject='Welcome to the Platform!',
            message='Your registration is successful as a Farmer. Please wait for approval.',
            from_email='admin@example.com',  # Email address used to send the message
            recipient_list=[user.email],  # Recipient's email address
            fail_silently=False,
        )

# API view for registering a new buyer
class BuyerRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Deserialize incoming user data using the UserSerializer
        user_serializer = UserSerializer(data=request.data)
        
        # Check if user data is valid
        if user_serializer.is_valid():
            # Create the user with user_type indicating they are a buyer
            user = user_serializer.save(user_type=3)  
            
            # Extract additional fields for Buyer profile
            phone = request.data.get('phone')
            address = request.data.get('address')
            delivery_method_id = request.data.get('default_delivery_method')

            # Retrieve the corresponding DeliveryMethod object
            delivery_method = None
            if delivery_method_id:
                try:
                    delivery_method = DeliveryMethod.objects.get(id=delivery_method_id)
                except DeliveryMethod.DoesNotExist:
                    return Response({'error': 'The specified delivery method does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

            # Create buyer profile including default delivery method
            Buyer.objects.create(
                user=user, 
                phone=phone, 
                address=address,
                default_delivery_method=delivery_method
            )
            
            # Return a success response
            return Response({'message': 'Buyer registered successfully!'}, status=status.HTTP_201_CREATED)
        
        # Return any errors in the data validation process
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API view for accessing farmer dashboard
class FarmerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request, *args, **kwargs):
        # Retrieve the farmer's profile based on the logged-in user
        farmer_profile = get_object_or_404(Farmer, user=request.user)
        serializer = FarmerSerializer(farmer_profile)  # Serialize the farmer profile data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Send serialized data as a response


# API view for accessing buyer dashboard
class BuyerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request, *args, **kwargs):
        # Retrieve the buyer's profile based on the logged-in user
        buyer_profile = get_object_or_404(Buyer, user=request.user)
        serializer = BuyerSerializer(buyer_profile)  # Serialize the buyer profile data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Send serialized data as a response