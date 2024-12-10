from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RegisterView, LoginView, UserViewSet

router = DefaultRouter()


router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += router.urls
