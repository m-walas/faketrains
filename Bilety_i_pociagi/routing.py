from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.urls import path

from .consumers import TrainSeatConsumer

websocket_urlpatterns = [
    path('ws/train_seat/', TrainSeatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    ),
})
