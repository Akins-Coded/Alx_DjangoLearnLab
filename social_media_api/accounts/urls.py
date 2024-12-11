from rest_framework.routers import DefaultRouter
from django.urls import path
from .import views

router = DefaultRouter()


router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),



    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow_user'),

]

urlpatterns += router.urls
