from django.urls import path
from .views import list_books, LibraryDetailView 


urlpatterns = [
    path('book/', views.list_books, name='Book Lists'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
[
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]