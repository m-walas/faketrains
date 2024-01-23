"""
ASGI config for bilety_kolejowe_projekt_pociagi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from Bilety_i_pociagi import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilety_kolejowe_projekt_pociagi.settings')

application = ProtocolTypeRouter({
    "https": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})