from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('books/', BookList.as_view(), name='book-list'), 
     path('', include(router.urls)),
]


urlpatterns += router.urls