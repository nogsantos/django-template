# -*- coding: utf-8 -*-
from core import views
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'core'

routers = DefaultRouter()
routers.register(
    'health-check', views.HealthCheckViewSet, base_name='core_health_check'
)

urlpatterns = [path('', include(routers.urls))]
