from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str:title>/<int:chapter_number>/', consumers.SceneConsumer.as_asgi())
]
