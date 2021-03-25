from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileReadOnlyViewSet, ProfileUpdateViewSet, PostViewSet, PostCreateAPIView, PostLikeAPIView, CommentCreateAPIView


router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')
router.register(r'profile', ProfileReadOnlyViewSet, basename='profile')
router.register(r'update-profile', ProfileUpdateViewSet , basename='profile-update')

urlpatterns = [

    path('', include(router.urls)),

    path('post-create', PostCreateAPIView.as_view(), name='post-create'),
    path('post-like/<slug:slug>/', PostLikeAPIView.as_view(), name='post-like'),

    path('comment-create/<slug:slug>/', CommentCreateAPIView.as_view(), name='comment-create'),

]