from rest_framework import generics, viewsets, mixins, permissions, filters
from rest_framework.response import Response
from api.models import Post, Likes, Comment, ArchivedPost
from api.serializers import PostSerializer, CommentSerializer, LikesSerializer
from api.permissions import IsOwnerOrReadOnly


class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)


class PostLikeAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)