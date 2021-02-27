from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(null=True, blank=True)
    biography = models.CharField(max_length=300, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self, **kwargs):
        return reverse('profile', kwargs={'slug': self.slug})