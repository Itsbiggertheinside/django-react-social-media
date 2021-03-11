from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, PostViewSet, PostCreateAPIView, PostLikeAPIView


router = DefaultRouter()
router.register('', PostViewSet, basename='post')
router.register('profile', ProfileViewSet, basename='profile')

urlpatterns = [

    path('', include(router.urls)),
    path('post-create', PostCreateAPIView.as_view(), name='post-create'),
    path('post-like', PostLikeAPIView.as_view(), name='post-like'),

]