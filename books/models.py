from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    published_date = models.DateField(verbose_name="Дата публикации")
    is_available = models.BooleanField(default=True, verbose_name="Доступна для продажи")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц")
    cover_image = models.ImageField(upload_to='books_covers/', blank=True, verbose_name="Обложка")
    book_file = models.FileField(upload_to='books_files/', blank=True, verbose_name="Электронный файл")
    discount_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Промокод (не обязательно)"
    )

    reserved_count = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name="Количество книг для брони"
    )

    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Просмотры"
    )

    def __str__(self):
        return self.title