from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(TestCase):
    def setUp(self):
        # Set up authenticated user
        self.client = APIClient()
        self.client.login = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.client.login(user=self.user)

        # Base URL for books API
        self.book_url = "/api/books/"
    
    def test_create_book(self):
        data = {"title": "Test Book", "author": "Author Name", "publication_year": 2023}
        response = self.client.post(self.book_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Test Book")

    def test_retrieve_book(self):
        book = Book.objects.create(title="Test Book", author="Author Name", publication_year=2023)
        response = self.client.get(f"{self.book_url}{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], book.title)

    def test_update_book(self):
        book = Book.objects.create(title="Old Title", author="Author Name", publication_year=2023)
        data = {"title": "Updated Title", "author": "Author Name", "publication_year": 2023}
        response = self.client.put(f"{self.book_url}{book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Title")

    def test_delete_book(self):
        book = Book.objects.create(title="Test Book", author="Author Name", publication_year=2023)
        response = self.client.delete(f"{self.book_url}{book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())

    def test_filter_books_by_author(self):
        Book.objects.create(title="Book 1", author="Author A", publication_year=2022)
        Book.objects.create(title="Book 2", author="Author B", publication_year=2023)
        response = self.client.get(f"{self.book_url}?author=Author A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author A")
