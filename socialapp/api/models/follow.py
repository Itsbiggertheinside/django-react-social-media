from django.db import models
from django.contrib.auth.models import User
from .profile import Profile


# class Follows(models.Model):
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

#     def __str__(self):
#         return '{}\'s follow list'.format(self.profile.slug)


# class Following(models.Model):
#     follows = models.ForeignKey(Follows, on_delete=models.CASCADE)
#     follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower')
#     followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followed')

#     def __str__(self):
#         return '{0} follow to {1}'.format(self.follower.slug, self.followed.slug)