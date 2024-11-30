from django.db import models

class DeliveryMethod(models.Model):
    DELIVERY_TYPE_CHOICES = [
        ('standard', 'Standard'),
        ('express', 'Express'),
        ('pickup', 'Pickup'),
    ]

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=DELIVERY_TYPE_CHOICES, default='standard')

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
