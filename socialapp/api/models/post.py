from django.db import models
from django.urls import reverse
from .profile import Profile



class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField()
    content = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return self.slug


class Likes(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{} likes {}\'s post'.format(self.profile.slug, self.post.profile.slug)


class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Post Id: {}, Author: {}, Comment: {}'.format(self.post.slug, self.profile.slug, self.content)


class ArchivedPost(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return '{}\'s archive'.format(self.profile.slug)