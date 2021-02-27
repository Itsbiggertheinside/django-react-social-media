from django.db import models
from django.urls import reverse
from .profile import Profile



class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField()
    content = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    # def get_absolute_url(self, **kwargs):
    #     return reverse('post', kwargs={'slug': self.slug})


class ArchivedPost(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)