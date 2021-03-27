from rest_framework import generics, status, viewsets, mixins, permissions, filters
from rest_framework.response import Response
from api.models import Profile, FollowingList, Followed
from api.serializers import FollowedProfilesPosts, FollowedsSerializer, FollowingListSerializer


class FollowingListViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        profile = self.request.query_params.get('profile', None)

        if profile is not None:
            return FollowingList.objects.filter(profile__user__username='root')

        return Followed.objects.filter(parent__profile__user__username='root')

    def get_serializer_class(self):
        profile = self.request.query_params.get('profile', None)

        if profile is not None:
            return FollowingListSerializer

        if self.action == 'list':
            return FollowedProfilesPosts
        return FollowedsSerializer