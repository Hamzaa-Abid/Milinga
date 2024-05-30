from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.sessions import SessionMiddlewareStack
from channels.auth import AuthMiddlewareStack
# from channels.auth import AuthMiddleware
from channels.security.websocket import AllowedHostsOriginValidator #, OriginValidator

from .consumers import Consumer

application = ProtocolTypeRouter({
    'websocket': 
    AllowedHostsOriginValidator(
        # AuthMiddleware(
        AuthMiddlewareStack(
        # SessionMiddlewareStack(
            URLRouter(
                [
                    url("ws/", Consumer)
                ]
            )
        # )
        )
        # )
    )
})