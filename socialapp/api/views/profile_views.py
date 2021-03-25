from rest_framework import generics, viewsets, mixins, permissions, filters, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.models import Profile
from api.serializers import ProfileUpdateSerializer, ProfilePictureUpdateSerializer, ProfileWithPostsSerializer, ProfileIsHiddenSerializer
from api.permissions import IsOwnerOrReadOnlyForProfile


class ProfileReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    lookup_field = 'user__username'

    def get_serializer_class(self):
        profile = self.get_object()
        if profile.is_hidden:
            serializer = ProfileIsHiddenSerializer
        return serializer


class ProfileUpdateViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    permission_classes = (IsOwnerOrReadOnlyForProfile, )
    lookup_field = 'user__username'

    def get_serializer_class(self):
        profile_picture = self.request.query_params.get('update-picture', None)
        if profile_picture is not None:
            return ProfilePictureUpdateSerializer
        return self.serializer_class