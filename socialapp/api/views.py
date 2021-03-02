from rest_framework import generics, viewsets, mixins, permissions, filters
from .models import Profile, Post
from .serializers import ProfileSerializer, ProfilePhotoSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly


class ProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # filter_backends = (filters.SearchFilter, )
    # search_fields = ('slug',)
    lookup_field = 'slug'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('user').prefetch_related('likes').all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    lookup_field = 'slug'

    # def get_queryset(self):
    #     queryset = Post.objects.all()
    #     username = self.request.query_params.get('username', None)
    #     if username is not None:
    #         queryset = queryset.filter(user__slug=username)
    #     return queryset
    
    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(user=profile)


class ProfilePhotoUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        profile = self.request.user.profile
        return profile
