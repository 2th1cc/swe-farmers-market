from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Buyer

@receiver(post_delete, sender=Buyer)
def delete_user_on_buyer_delete(sender, instance, **kwargs):
    instance.user.delete()
