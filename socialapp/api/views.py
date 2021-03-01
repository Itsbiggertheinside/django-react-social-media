from rest_framework import viewsets, mixins
from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly


class ProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    lookup_field = 'slug'


class PostViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    lookup_field = 'slug'
    
    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(user=profile)