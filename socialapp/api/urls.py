from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, PostViewSet, ProfilePhotoUpdateAPIView

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('profile-photo/update/', ProfilePhotoUpdateAPIView.as_view(), name='profile-photo-update'),
]