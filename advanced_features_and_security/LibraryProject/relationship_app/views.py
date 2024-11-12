from django.shortcuts import render, get_object_or_404, redirect
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.http import HttpResponseForbidden
 

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




# Helper functions to check the user's role
def is_admin(user):
    return user.profile.role == 'Admin'

def is_librarian(user):
    return user.profile.role == 'Librarian'

def is_member(user):
    return user.profile.role == 'Member'

# Admin view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# View for adding a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

# View for editing an existing book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

# View for deleting a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})