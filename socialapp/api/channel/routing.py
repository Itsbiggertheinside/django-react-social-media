from django.urls import re_path
from .consumers import DirectConsumer

websocket_urlpatterns = [
    re_path(r'ws/direct/(?P<direct_code>\w+)/$', DirectConsumer.as_asgi()),
]