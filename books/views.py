from django.views import generic
from django.shortcuts import redirect
from django.db.models import Q
from .models import Book
from django.db.models import F


class HomeView(generic.TemplateView):
    template_name = "home.html"


class BookListView(generic.ListView):
    template_name = "books_list.html"
    model = Book
    paginate_by = 2
    ordering = ["-id"]

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = context["page_obj"]
        return context


class BookDetailView(generic.DetailView):
    template_name = "books_detail.html"
    context_object_name = "book"
    model = Book
    pk_url_kwarg = "pk"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request
        viewed_books = request.session.get("viewed_books", [])

        if obj.pk not in viewed_books:
            self.model.objects.filter(pk=obj.pk).update(
                views=F("views") + 1
            )
            viewed_books.append(obj.pk)
            request.session["viewed_books"] = viewed_books
            obj.refresh_from_db()

        return obj


class BookCreateView(generic.CreateView):
    model = Book
    template_name = "book_form.html"

    fields = [
        "title",
        "author",
        "description",
        "price",
        "published_date",
        "is_available",
        "pages",
        "cover_image",
        "book_file",
        "discount_code",
        "reserved_count",
    ]

    success_url = "/books/"


class SearchBookView(generic.ListView):
    template_name = "books_list.html"
    model = Book
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get("s")

        if query:
            return self.model.objects.filter(
                Q(title__icontains=query) |
                Q(author__icontains=query)
            )

        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = context["page_obj"]
        context["s"] = self.request.GET.get("s")
        return context 