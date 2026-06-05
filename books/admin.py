from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'is_available', 'reserved_count')
    list_filter = ('is_available', 'published_date')
    search_fields = ('title', 'author')
