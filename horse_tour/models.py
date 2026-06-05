from django.db import models

class Tourist(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="ФИО туриста")
    passport_id = models.CharField(max_length=20, unique=True, verbose_name="Персональный номер")

    def __str__(self):
        return self.fullname

class Horse(models.Model):
    name = models.CharField(max_length=50, verbose_name="Кличка лошади")
    booked_by = models.OneToOneField(Tourist, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Забронирована туристом")

    def __str__(self):
        return self.name

class TourCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Категория")

    def __str__(self):
        return self.name

class HorseTour(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название тура")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена тура")
    categories = models.ManyToManyField(TourCategory, verbose_name="Категории")

    def __str__(self):
        return self.title

class Comment(models.Model):
    tour = models.ForeignKey(HorseTour, on_delete=models.CASCADE, related_name='comments', verbose_name="Тур")
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий к {self.tour.title}"
