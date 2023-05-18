from django.contrib.auth import hashers
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import User


@receiver(pre_save, sender=User)
def hash_password(sender, instance, **kwargs):
    if not instance.pk:
        instance.password = hashers.make_password(instance.password)
