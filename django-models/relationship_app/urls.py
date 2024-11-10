from django.urls import path
from .views import list_books, LibraryDetailView 


urlpatterns = [
    path('book/', views.list_books, template_name ='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), template_name='library_detail'),
]
[
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]