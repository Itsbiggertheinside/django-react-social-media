from rest_framework import generics, viewsets, mixins, permissions, filters
from rest_framework.response import Response
from api.models import Post, Comment
from api.serializers import CommentSerializer, LikesSerializer
from api.permissions import IsOwnerOrReadOnly



class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_slug = self.kwargs.get('slug')
        post = generics.get_object_or_404(Post, slug=post_slug)
        profile = self.request.user.profile
        serializer.save(profile=profile, post=post)


# class CommentLikeAPIView(generics.CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = LikesSerializer

#     def perform_create(self, serializer):
#         profile = self.request.user.profile
#         serializer.save(profile=profile)