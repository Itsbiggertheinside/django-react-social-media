from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileReadOnlyViewSet, ProfileUpdateViewSet, PostViewSet, PostLikeViewSet, CommentCreateAPIView, FollowingListViewSet, DirectChannelViewSet, DirectMessageCreateViewSet
# from api.channel.views import DirectViewSet



router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'create/like', PostLikeViewSet, basename='like')
router.register(r'following', FollowingListViewSet, basename='following')
router.register(r'profile', ProfileReadOnlyViewSet, basename='profile')
router.register(r'update-profile', ProfileUpdateViewSet , basename='update-profile')
router.register(r'direct/channel', DirectChannelViewSet , basename='direct-channel')
router.register(r'direct/message', DirectMessageCreateViewSet , basename='direct-message')

urlpatterns = [

    path('', include(router.urls)),

    path('comment-create/<slug:slug>/', CommentCreateAPIView.as_view(), name='comment-create'),

]