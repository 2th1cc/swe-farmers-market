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
from .serializers import EmailAuthTokenSerializer
from django.db import transaction
from django.db.models import ObjectDoesNotExist

# Endpoint for user login using token authentication
class LoginAPIView(ObtainAuthToken):
    serializer_class = EmailAuthTokenSerializer
    
    def post(self, request):
        print("Received payload:", request.data)
        # Use the DRF's built-in serializer for handling login data (username/password)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)  # Validate data and raise an error if invalid
        user = serializer.validated_data['user']  # Retrieve the authenticated user from validated data
        token, created = Token.objects.get_or_create(user=user)  # Get or create an authentication token for the user
        print(f"Token for {user.email}: {token.key}")
        redirect_url = {
            1: "https://web-app.example.com/admin-dashboard",
            2: "/api/dashboard/farmer/",
            3: "/api/dashboard/buyer/"
        }.get(user.user_type, None)

        if not redirect_url:
            return Response({"error": "Invalid user type."}, status=status.HTTP_400_BAD_REQUEST)

        print("Validation errors:", serializer.errors)
        return Response({
            "token": token.key,
            "user_type": user.user_type,
            "redirect_url": redirect_url
        }, status=status.HTTP_200_OK)  # Return the token to the client
        
# API view for registering a new farmer
class FarmerRegistrationAPIView(APIView):
    def post(self, request):
        try:
            # Start a transaction block
            with transaction.atomic():
                # Deserialize and validate user data
                user_serializer = UserSerializer(data=request.data)
                if not user_serializer.is_valid():
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                # Create the user with user_type indicating they are a farmer
                user = user_serializer.save(user_type=2)

                # Collect additional farmer-specific fields
                phone = request.data.get('phone')
                farm_name = request.data.get('farm_name')
                farm_location = request.data.get('farm_location')
                farm_size = request.data.get('farm_size')
                soil_type = request.data.get('soil_type', 1)

                valid_soil_types = [choice[0] for choice in Farmer._meta.get_field('soil_type').choices]
                if soil_type not in valid_soil_types:
                    raise ValueError(f"Invalid soil type. Valid values are: {valid_soil_types}")

                # Validate required fields
                if not phone:
                    raise ValueError("Phone is required.")
                if not farm_name:
                    raise ValueError("Farm name is required.")

                # Create farmer profile with validated fields
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
        except ValueError as e:
            # Handle validation errors and ensure the database is rolled back
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

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
    def post(self, request):
        # Start a database transaction
        try:
            with transaction.atomic():
                data = request.data
                data['user_type'] = 3 
                # Deserialize incoming user data using the UserSerializer
                user_serializer = UserSerializer(data=request.data)

                # Check if user data is valid
                if not user_serializer.is_valid():
                    print("Received data:", request.data)
                    print("Validation errors:", user_serializer.errors)
                    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # Create the user with user_type indicating they are a buyer
                user = user_serializer.save(user_type=3)

                # Extract additional fields for Buyer profile
                phone = request.data.get('phone')
                if not phone:
                    raise ValueError("Phone is required.")

                address = request.data.get('address', "")
                delivery_method_id = request.data.get('default_delivery_method')

                # Retrieve the corresponding DeliveryMethod object
                delivery_method = None
                if delivery_method_id:
                    try:
                        delivery_method = DeliveryMethod.objects.get(id=delivery_method_id)
                    except ObjectDoesNotExist:
                        raise ValueError("The specified delivery method does not exist.")
                else:
                    # Assign a default delivery method (e.g., Standard)
                    delivery_method = DeliveryMethod.objects.filter(type="standard").first()
                    if not delivery_method:
                        raise ValueError("No default delivery methods available. Please add one.")
    
                # Create buyer profile including default delivery method
                Buyer.objects.create(
                    user=user,
                    phone=phone,
                    address=address,
                    default_delivery_method=delivery_method
                )

                # If everything is successful, return a success response
                return Response({'message': 'Buyer registered successfully!'}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            # Handle validation errors and ensure the database is rolled back
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# API view for accessing farmer dashboard
class FarmerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request):
        # Retrieve the farmer's profile based on the logged-in user
        farmer_profile = get_object_or_404(Farmer, user=request.user)
        serializer = FarmerSerializer(farmer_profile)  # Serialize the farmer profile data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Send serialized data as a response

# API view for accessing buyer dashboard
class BuyerDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def get(self, request):
        # Retrieve the buyer's profile based on the logged-in user
        buyer_profile = get_object_or_404(Buyer, user=request.user)
        serializer = BuyerSerializer(buyer_profile)  # Serialize the buyer profile data
        return Response(serializer.data, status=status.HTTP_200_OK)  # Send serialized data as a response

class AdminBuyerListView(APIView):
    """View all buyers or a specific buyer"""
    permission_classes = [IsAuthenticated]

    def get(self, request, buyer_id=None):
        # View all buyers
        if buyer_id is None:
            buyers = Buyer.objects.all()
            serializer = BuyerSerializer(buyers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # View a specific buyer
        buyer = get_object_or_404(Buyer, id=buyer_id)
        serializer = BuyerSerializer(buyer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminFarmerListView(APIView):
    """View all farmers or a specific farmer"""
    permission_classes = [IsAuthenticated]

    def get(self, request, farmer_id=None):
        # View all farmers
        if farmer_id is None:
            farmers = Farmer.objects.all()
            serializer = FarmerSerializer(farmers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # View a specific farmer
        farmer = get_object_or_404(Farmer, id=farmer_id)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminEditUserView(APIView):
    """Edit a buyer or farmer"""
    permission_classes = [IsAuthenticated]

    def put(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDeleteUserView(APIView):
    """Delete a buyer or farmer"""
    permission_classes = [IsAuthenticated]

    def delete(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class AdminToggleUserStatusView(APIView):

    """Enable or disable a user account"""
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.is_active = not user.is_active  # Toggle status
        user.save()
        status_message = "enabled" if user.is_active else "disabled"
        return Response({"message": f"User account has been {status_message}."}, status=status.HTTP_200_OK)

class CreateAdminAPIView(APIView):
    def post(self, request):
        data = request.data
        data['user_type'] = 1  # Set user_type to admin
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save(is_superuser=False, is_staff=True)  # Make staff but not superuser
            return Response({"message": "Admin created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
