import os
import django
from api.channel import token_auth_middleware, routing

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter



from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialapp.settings')
django.setup()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': token_auth_middleware.TokenAuthMiddlewareStack(
        URLRouter(routing.websocket_urlpatterns)
    ),
})
