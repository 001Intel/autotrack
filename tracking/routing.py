# tracking/routing.py
from django.urls import re_path
from .consumers import PackageTrackingConsumer

websocket_urlpatterns = [
    re_path(r'ws/tracking/(?P<tracking_id>[0-9a-f-]+)/$', PackageTrackingConsumer.as_asgi()),
]
