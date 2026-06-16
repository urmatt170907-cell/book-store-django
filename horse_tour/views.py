from django.shortcuts import render, redirect, get_object_or_404
from .models import HorseTour, Horse, Tourist, Comment, TourCategory
from django.core.paginator import Paginator


def horse_tour_view(request):
    search = request.GET.get('s')

    if search:
        tours = HorseTour.objects.filter(
            title__icontains=search
        )
    else:
        tours = HorseTour.objects.all()

    paginator = Paginator(tours, 5)
    page = request.GET.get('page')
    tours = paginator.get_page(page)

    horses = Horse.objects.all()
    tourists = Tourist.objects.all()
    categories = TourCategory.objects.all()

    return render(
        request,
        'tours.html',
        {
            'tours': tours,
            'horses': horses,
            'tourists': tourists,
            'categories': categories,
            's': search
        }
    )


def create_tour_category_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            TourCategory.objects.create(name=name)

    return redirect('horse_tours')


def create_horse_tour_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        category_ids = request.POST.getlist('categories')

        if title and price:
            tour = HorseTour.objects.create(
                title=title,
                price=price
            )

            if category_ids:
                tour.categories.set(category_ids)

    return redirect('horse_tours')


def create_horse_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if name:
            Horse.objects.create(name=name)

    return redirect('horse_tours')


def book_horse_view(request):
    if request.method == 'POST':
        horse_id = request.POST.get('horse_id')
        fullname = request.POST.get('fullname')
        passport_id = request.POST.get('passport_id')

        tourist, created = Tourist.objects.get_or_create(
            passport_id=passport_id,
            defaults={'fullname': fullname}
        )

        horse = get_object_or_404(Horse, id=horse_id)
        horse.booked_by = tourist
        horse.save()

    return redirect('horse_tours')


def add_comment_view(request):
    if request.method == 'POST':
        tour_id = request.POST.get('tour_id')
        text = request.POST.get('text')

        tour = get_object_or_404(HorseTour, id=tour_id)

        Comment.objects.create(
            tour=tour,
            text=text
        )

    return redirect('horse_tours')