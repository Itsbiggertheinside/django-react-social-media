from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly



class DevProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_object(self, slug=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Profile, slug=slug)

    def put(self, request, *args, **kwargs):
        return super(DevProfileApiView, self).update(request, *args, **kwargs)


class DevPostApiView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get(self, request, *args, **kwargs):
        return super(DevPostApiView, self).list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DevPostApiView, self).create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.profile)