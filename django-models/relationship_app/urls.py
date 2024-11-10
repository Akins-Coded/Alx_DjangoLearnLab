# relationship_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView

urlpatterns = [
    
    path('book/', views.list_books, name='book_list'),
    path('book/add/', views.add_book, name='add_book'),  
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),  
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),


    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('/', views.home, name='home'),
    
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
