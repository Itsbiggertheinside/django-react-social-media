from django.db import models
from django.contrib.auth.models import User
from .profile import Profile


class Follow(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    followers_list = models.ManyToManyField(Profile, null=True, blank=True, related_name='followers')
    followeds_list = models.ManyToManyField(Profile, null=True, blank=True, related_name='followeds')

    def __str__(self):
        return '{}\'s follow list'.format(self.user.slug)