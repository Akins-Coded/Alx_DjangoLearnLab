from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm, BookSearchForm
# View to create a book (only users with can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        book = Book.objects.create(title=title, content=content)
        return redirect('book_detail', pk=book.pk)  # Make sure 'book_detail' is the correct URL name
    return render(request, 'create_book.html')

# View to edit a book (only users with can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.content = request.POST.get('content')
        book.save()
        return redirect('book_detail', pk=book.pk)
    return render(request, 'edit_book.html', {'book': book})

# View to delete a book (only users with can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

# View to view a book (only users with can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'view_book.html', {'book': book})

# View to list and search books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    form = BookSearchForm(request.GET)
    books = None  # Initialize the books variable

    if form.is_valid():
        query = form.cleaned_data['search_query']
        books = Book.objects.filter(title__icontains=query)
    else:
        # If the form is not valid, fetch all books
        books = Book.objects.all()

    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
