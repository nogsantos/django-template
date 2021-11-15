# -*- coding: utf-8 -*-
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views import CheckViewSet

routers = DefaultRouter()
routers.register('', CheckViewSet, basename='core')

urlpatterns = [path('', include(routers.get_urls()))]
