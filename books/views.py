from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book

def home_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')

def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'books_list.html', {'books': books})

def book_create_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        published_date = request.POST.get('published_date')
        pages = request.POST.get('pages')
        reserved_count = request.POST.get('reserved_count')
        discount_code = request.POST.get('discount_code') or None
        cover_image = request.FILES.get('cover_image')
        book_file = request.FILES.get('book_file')

        Book.objects.create(
            title=title, author=author, description=description, price=price,
            published_date=published_date, pages=pages, reserved_count=reserved_count,
            discount_code=discount_code, cover_image=cover_image, book_file=book_file
        )
        return redirect('book_list')
    return render(request, 'book_form.html')

def book_detail_view(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books_detail.html', {'book': book})
