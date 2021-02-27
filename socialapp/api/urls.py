from django.urls import path
from .views import DevProfileApiView, DevPostApiView

urlpatterns = [

    path('profile/<slug:slug>/', DevProfileApiView.as_view(), name='profile'),
    path('posts/', DevPostApiView.as_view(), name='post-list'),

]