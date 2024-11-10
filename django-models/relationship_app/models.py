from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="Book")

class Library(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name="Library")  

class Librarian(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="Librarian")

    def __str__(self):
        return self.name 