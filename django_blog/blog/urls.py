from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register, profile, search, PostByTagListView, PostViewSet, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView
from rest_framework.routers import DefaultRouter

# Registering the API viewset
router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    # API routes
    path('api/', include(router.urls)),

    # Authentication routes
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Registration 
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('search/', search, name='search'),
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view()),
    
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
