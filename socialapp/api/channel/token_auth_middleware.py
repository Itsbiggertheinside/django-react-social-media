from channels.auth import AuthMiddlewareStack
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections



class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        if b'Authorization' in headers:
            token_name, token_key = await headers[b'Authorization'].decode().split()
            if token_name == 'Token':
                try:
                    token = await Token.objects.get(key=token_key)
                    scope['user'] = await token.user
                    close_old_connections()
                except Token.DoesNotExist:
                    scope['user'] = await AnonymousYser()
        return await self.inner(scope, receive, send)


TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))
# def TokenAuthMiddlewareStack(inner):
#   return TokenAuthMiddleware(AuthMiddlewareStack(inner))