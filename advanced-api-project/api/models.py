from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_year = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')  # Use lowercase and ensure 'Author' is defined.

    def __str__(self):
        return f"{self.title} published in the year {self.publication_year} by {self.author}"

    class Meta:
        permissions = [  
            ("CreateView", "Can Create"),
            ("UpdateView", "Can Update"),
            ("DeleteView", "Can Delete"),
            ]

