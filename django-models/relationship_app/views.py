from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView
 

# Create your views here.
def home(request):
    return render(request, 'relationship_app/home.html')

def list_books(request):
    books = Book.objects.all()
    context = {'book_list' : books}
    return render (request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
     
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  
        books_in_library = Book.objects.filter(library=library)
        average_rating = books_in_library.aggregate(average_rating=models.Avg('rating'))['average_rating']
        context['books'] = books_in_library
        context['average_rating'] = average_rating()

        return context