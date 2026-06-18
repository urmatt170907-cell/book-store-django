from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="minutes")
    country = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.TextField()
    rating = models.FloatField()
    trailer_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class VIPSeat(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)