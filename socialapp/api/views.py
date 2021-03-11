from rest_framework import generics, viewsets, mixins, permissions, filters
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile, Post, Likes, Comment, ArchivedPost, Follows, Following
from .serializers import UserSerializer, ProfileSerializer, PostSerializer, FollowsSerializer, FollowingSerializer, CommentSerializer, LikesSerializer
from .permissions import IsOwnerOrReadOnly


class ProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    lookup_field = 'username'


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
    serializer_class = LikesSerializer

    def get_object(self, pk=None):
        return generics.get_object_or_404(Post, pk=pk)

    def perform_create(self, serializer):
        profile = self.request.user.profile
        post = self.get_object()
        serializer.save(profile=profile)