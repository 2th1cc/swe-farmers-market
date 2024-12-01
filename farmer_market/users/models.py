from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from orders.models import DeliveryMethod 
from django.core.validators import RegexValidator
#baseuser is used to create users and superusers
#abstractuser allows customization; has all fields and methods of default user
# Custom user manager for farmers and buyers
#HOW users are created
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, user_type=3, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, user_type=1, **extra_fields)
# Custom user model for farmers and buyers
# User model
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'farmer'),
        (3, 'buyer'),
    )
    is_active = models.BooleanField(default=True)

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    USERNAME_FIELD = 'email'  # Use email for authentication instead of username
    REQUIRED_FIELDS = ['username']
    # Specify related_name to avoid conflicts with the default User model
    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Farmer model
class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Each crop has a unique name

    def __str__(self):
        return self.name
    
class Farmer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='farmer')
    registration_date = models.DateField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    phone = models.CharField(max_length=15) 
    rejection_feedback = models.TextField(blank=True, null=True)  # For optional rejection feedback
    farm_name = models.CharField(max_length=255, blank=True, null=True)
    farm_location = models.CharField(max_length=255, blank=True, null=True)
    farm_size = models.CharField(max_length=100, blank=True, null=True)
    farm_description = models.TextField(blank=True, null=True)
    crops_grown = models.ManyToManyField(Crop, related_name="farmers")  # Many-to-many relationship
    soil_type = models.PositiveIntegerField(choices=[
        (1, 'Sandy'),
        (2, 'Clay'),
        (3, 'Loamy'),
        (4, 'Silty'),
        (5, 'Peaty'),
        (6, 'Chalky'),
    ], default=1)

    def __str__(self):
        return self.user.email

# Buyer model
class Buyer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='buyer')
    registration_date = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    preferred_payment_method = models.CharField(max_length=50, blank=True, null=True)
    default_delivery_method = models.ForeignKey(DeliveryMethod, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.user.email