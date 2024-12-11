from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'notifications', views.NotificationViewSet, basename='notification')

# Add the router URLs to the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
