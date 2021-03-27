from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileReadOnlyViewSet, ProfileUpdateViewSet, PostViewSet, PostCreateAPIView, PostLikeViewSet, CommentCreateAPIView, FollowingListViewSet


router = DefaultRouter()
router.register(r'create/like', PostLikeViewSet, basename='like')
router.register(r'following', FollowingListViewSet, basename='following')
router.register(r'profile', ProfileReadOnlyViewSet, basename='profile')
router.register(r'update-profile', ProfileUpdateViewSet , basename='update-profile')
router.register(r'', PostViewSet, basename='post')

urlpatterns = [

    path('', include(router.urls)),

    path('create/post/', PostCreateAPIView.as_view(), name='post-create'),

    path('comment-create/<slug:slug>/', CommentCreateAPIView.as_view(), name='comment-create'),

]