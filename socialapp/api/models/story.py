from django.db import models
from .profile import Profile


class Story(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='stories')
    story = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile}\'s Story'