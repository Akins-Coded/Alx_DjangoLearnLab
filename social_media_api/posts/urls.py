from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments', views.CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),

    path('feed/', views.FeedViewSet.as_view(), name='feed'),

    path('<int:pk>/like/', views.LikeViewSet.as_view({'post': 'create'}), name='like_post'),
    path('<int:pk>/unlike/', views.LikeViewSet.as_view({'post': 'destroy'}), name='unlike_post'),

]
urlpatterns = [
    path('', views.NotificationViewSet.as_view({'get': 'list'}), name='get_notifications'),
]