"""
ASGI config for bilety_kolejowe_projekt_pociagi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilety_kolejowe_projekt_pociagi.settings')

django_asgi_app = get_asgi_application()

import Bilety_i_pociagi.routing as routing

application = ProtocolTypeRouter(
    {
        'http': django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))),
    }
)