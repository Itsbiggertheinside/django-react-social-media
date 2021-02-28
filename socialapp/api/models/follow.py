from django.db import models
from .profile import Profile


class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE)
    followed = models.ManyToManyField(Profile, related_name='followed')

    def __str__(self):
        return '{}\'s followed list'.format(self.follower)