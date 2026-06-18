from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect

from .models import Movie, Comment
from .forms import MovieForm, CommentForm


# LIST
class MovieListView(ListView):
    model = Movie
    template_name = 'cineboard/movie_list.html'
    context_object_name = 'movies'


# DETAIL
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'cineboard/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


# CREATE
class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'
    success_url = reverse_lazy('movie_list')


# UPDATE
class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cineboard/movie_form.html'
    success_url = reverse_lazy('movie_list')


# DELETE
class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'cineboard/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


# COMMENT ADD (простая FBV — нормально для учебного проекта)
def add_comment(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()

    return redirect('movie_detail', pk=pk)