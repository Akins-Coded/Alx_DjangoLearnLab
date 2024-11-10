from django.urls import path
from . import views


urlpatterns = [
    path('book/', views.book_list, name='Book Lists'),
    path('library/<int:pk>/', views.libraryDetails.as_view(), name='library_detail'),
]