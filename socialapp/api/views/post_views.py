from rest_framework import generics, status, viewsets, mixins, permissions, filters
from rest_framework.response import Response
from api.models import Profile, Post, Likes, Comment, ArchivedPost
from api.serializers import PostSerializer, CommentSerializer, LikesSerializer, FollowedsSerializer
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


class PostLikeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer

    def create(self, request, *args, **kwargs):
        post = Post.objects.get(slug=request.data['post'])
        profile = Profile.objects.get(slug=request.data['profile'])
        like, created = Likes.objects.get_or_create(post=post, profile=profile)
        serializer = self.serializer_class(like)
        if not created:
            like.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        