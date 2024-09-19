from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from server.presentations.api.views import PresentationListAPIView

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


app_name = "api"

urlpatterns = [
    path("presentations/", PresentationListAPIView.as_view()),
]
