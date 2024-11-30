from rest_framework import serializers
from .models import DeliveryMethod

class DeliveryMethodSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_display', read_only=True)  # Human-readable type

    class Meta:
        model = DeliveryMethod
        fields = ['id', 'name', 'description', 'type', 'type_display']

