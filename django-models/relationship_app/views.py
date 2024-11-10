from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

 

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
    
# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to homepage after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# Registration view
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})