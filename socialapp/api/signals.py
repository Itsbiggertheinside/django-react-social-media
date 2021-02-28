from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from .models import Profile, Follow



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    random_slug = str(uuid4().hex[:16])
    if created:
        Profile.objects.create(user=instance, slug=random_slug)

@receiver(post_save, sender=Profile)
def create_follow(sender, instance, created, **kwargs):
    if created:
        Follow.objects.create(user=instance)