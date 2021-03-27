from django.contrib import admin
from .models import Profile, Post, Likes, Comment, ArchivedPost, FollowingList, Follower, Followed

# Register your models here.
admin.site.register(Profile)
admin.site.register(FollowingList)
admin.site.register(Follower)
admin.site.register(Followed)
admin.site.register(Post)
admin.site.register(ArchivedPost)
admin.site.register(Likes)
admin.site.register(Comment)