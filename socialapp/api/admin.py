from django.contrib import admin
from .models import Profile, Post, Likes, Comment, ArchivedPost, Follows, Following

# Register your models here.
admin.site.register(Profile)
admin.site.register(Follows)
admin.site.register(Following)
admin.site.register(Post)
admin.site.register(ArchivedPost)
admin.site.register(Likes)
admin.site.register(Comment)