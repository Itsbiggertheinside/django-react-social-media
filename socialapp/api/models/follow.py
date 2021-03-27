from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from .profile import Profile


class FollowingList(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username}\'s follow list'


class Follower(models.Model):
    parent = ForeignKey(FollowingList, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.follower.user.username} follow {self.parent.profile.user.username}'


class Followed(models.Model):
    parent = ForeignKey(FollowingList, on_delete=models.CASCADE, related_name='followeds')
    followed = ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.parent.profile.user.username} follow {self.followed.user.username}'