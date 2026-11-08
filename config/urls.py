"""URL configuration for the minimal project."""

from django.urls import path

from health.views import health_check

urlpatterns = [path("health/", health_check, name="health_check")]
