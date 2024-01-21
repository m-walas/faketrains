"""
ASGI config for bilety_kolejowe_projekt_pociagi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from Bilety_i_pociagi import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilety_kolejowe_projekt_pociagi.settings')

application = get_asgi_application()

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
