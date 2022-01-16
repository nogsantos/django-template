from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core import views

routers = DefaultRouter()
routers.register("", views.HealthCheckViewSet, basename="core")

urlpatterns = [path("", include(routers.get_urls()))]
