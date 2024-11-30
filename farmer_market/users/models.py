from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from orders.models import DeliveryMethod 

# Custom user manager for farmers and buyers
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

# Custom user model for farmers and buyers
class CustomUser(AbstractUser):
    from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (2, 'farmer'),
        (3, 'buyer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)
    email = models.EmailField(unique=True)

    # Specify related_name to avoid conflicts with the default User model
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # Custom related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_set',  # Custom related name
        blank=True
    )

    objects = CustomUserManager()

# Farmer model
class Farmer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='farmer_profile')
    phone = models.CharField(max_length=15)
    registration_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    rejection_feedback = models.TextField(blank=True, null=True)  # For optional rejection feedback
    farm_name = models.CharField(max_length=255, blank=True, null=True)
    farm_location = models.CharField(max_length=255, blank=True, null=True)
    farm_size = models.CharField(max_length=100, blank=True, null=True)

# Buyer model
class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='buyer_profile')
    phone = models.CharField(max_length=15)
    registration_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=255)
    default_delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.SET_NULL, null=True)
