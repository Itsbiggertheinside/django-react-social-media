from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


GENDER_CHOICE = [
    ('M', 'Erkek'),
    ('F', 'Kadın'),
    ('U', 'Bilinmiyor')
]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    picture = models.ImageField(null=True, blank=True)
    biography = models.CharField(max_length=300, null=True, blank=True)
    webpage = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default='U')
    phone = models.CharField(max_length=11, null=True, blank=True)
    is_hidden = models.BooleanField(default=False)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return self.user.username + '\'s profile'

    @property
    def get_username(self):
        return self.user.username