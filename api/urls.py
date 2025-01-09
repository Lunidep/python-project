from django.urls import path
from .views import PingPongController

urlpatterns = [
    path('ping', PingPongController.as_view(), name='ping'),
    path('pong', PingPongController.as_view(), name='pong'),
]
