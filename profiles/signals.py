
from django.db.models.signals import post_save, post_delete

from django.dispatch import receiver

from django.contrib.auth.models import User

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username
        )

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance,**kwargs):
    instance.user.delete()
    print(f'user {instance.username} was deleted.')