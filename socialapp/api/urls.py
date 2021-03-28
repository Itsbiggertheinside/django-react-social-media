from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileReadOnlyViewSet, ProfileUpdateViewSet, PostViewSet, PostLikeViewSet, CommentCreateAPIView, FollowingListViewSet


router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'create/like', PostLikeViewSet, basename='like')
router.register(r'following', FollowingListViewSet, basename='following')
router.register(r'profile', ProfileReadOnlyViewSet, basename='profile')
router.register(r'update-profile', ProfileUpdateViewSet , basename='update-profile')

urlpatterns = [

    path('', include(router.urls)),

    path('comment-create/<slug:slug>/', CommentCreateAPIView.as_view(), name='comment-create'),

]