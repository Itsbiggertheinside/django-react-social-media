from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView, Response
from .models import Profile, Post
from .serializers import ProfileSerializer, PostSerializer



class DevProfileApiView(APIView):
    
    def get(self, request, slug=None):
        profile = get_object_or_404(Profile, slug=slug)
        serializer = ProfileSerializer(instance=profile)
        return Response(serializer.data)


class DevPostApiView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(instance=posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)