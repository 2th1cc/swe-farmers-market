from rest_framework import serializers
from .models import Product, ProductImage, LowStockNotification

# Serializer for ProductImage model
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image']

# Serializer for Product model
class ProductSerializer(serializers.ModelSerializer):
    # Nested serializer for images related to the product
    images = ProductImageSerializer(many=True, read_only=True)
    
    # List field to handle image uploads as a list of image files; write-only field
    image_uploads = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Product  # Model to serialize
        fields = ['id', 'user', 'name', 'category', 'description', 'price', 'quantity', 
                  'is_out_of_stock', 'images', 'image_uploads']  # Fields to include in serialization

        # Fields that cannot be changed through this serializer
        read_only_fields = ['user', 'is_out_of_stock']

    # Method to create a new product instance
    def create(self, validated_data):
        # Extract and remove 'image_uploads' data from validated data
        images_data = validated_data.pop('image_uploads')
        
        # Create a new Product instance with the remaining validated data
        product = Product.objects.create(**validated_data)
        
        # Iterate over each image in the images_data list
        for image_data in images_data:
            # Create a new ProductImage instance related to the product
            ProductImage.objects.create(product=product, image=image_data)
        
        return product

    # Method to update an existing product instance
    def update(self, instance, validated_data):
        # Extract 'image_uploads' data if provided; default to None if not
        images_data = validated_data.pop('image_uploads', None)
        
        if images_data:
            # Delete existing images associated with the product
            instance.images.all().delete()
            # Create new ProductImage instances for each image in the new data
            for image_data in images_data:
                ProductImage.objects.create(product=instance, image=image_data)

        # Update other fields of the instance with new values from validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        # Save the updated instance to the database
        instance.save()
        return instance

class LowStockNotificationSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = LowStockNotification
        fields = ['id', 'product', 'product_name', 'is_read', 'created_at']