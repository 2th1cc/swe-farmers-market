from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('vegetables', 'Vegetables'),
        ('fruits', 'Fruits'),
        ('seeds', 'Seeds'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')  # Reference to the farmer/user
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    is_out_of_stock = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Automatically sets the product as out of stock if the quantity is zero or less
        self.is_out_of_stock = self.quantity <= 0
        super().save(*args, **kwargs)  # Calls the super class's save method to save the instance to the database
        check_and_create_low_stock_notification(self)  # Check and create notification if necessary

    def __str__(self):
        # String representation of the Product object, typically used in Django admin
        return self.name

def check_and_create_low_stock_notification(product):
    LOW_STOCK_THRESHOLD = 10  # Example threshold

    if product.quantity < LOW_STOCK_THRESHOLD:
        notification_exists = LowStockNotification.objects.filter(
            farmer=product.user,
            product=product,
            is_read=False
        ).exists()

        if not notification_exists:
            LowStockNotification.objects.create(
                farmer=product.user,
                product=product
            )

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first to ensure the image file path is available
        
        # Open the image using Pillow and resize if necessary
        img = Image.open(self.image.path)
        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        # String representation of the ProductImage object
        return f"Image for {self.product.name}"

class LowStockNotification(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


