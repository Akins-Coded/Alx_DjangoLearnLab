from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to create an article (only users with can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        booK = Book.objects.create(title=title, content=content)
        return redirect('Book_detail', pk=Book.pk)
    return render(request, 'create_book.html')

# View to edit an article (only users with can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.content = request.POST.get('content')
        book.save()
        return redirect('article_detail', pk=book.pk)
    return render(request, 'edit_article.html', {'article': book})

# View to delete an article (only users with can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

# View to view an article (only users with can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'view_book.html', {'book': book})
