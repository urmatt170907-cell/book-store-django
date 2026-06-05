from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def all_categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories': categories})

def all_products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})

def category_products_view(request, category_id):
    if request.method == 'GET':
        category = get_object_or_404(Category, id=category_id)
        products = category.products.all()
        return render(request, 'category_products.html', {'category': category, 'products': products})
def home_view(request):
    if request.method == 'GET':
        return render(request, 'home.html')
