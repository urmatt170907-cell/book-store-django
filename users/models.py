from django.db import models


class Candidate(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    age = models.PositiveIntegerField(verbose_name="Возраст")
    gender = models.CharField(max_length=20, verbose_name="Пол")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    education = models.CharField(max_length=255, verbose_name="Образование")
    profession = models.CharField(max_length=255, verbose_name="Профессия")
    experience = models.TextField(verbose_name="Опыт работы")
    login = models.CharField(max_length=100, unique=True, verbose_name="Логин")
    password = models.CharField(max_length=100, verbose_name="Пароль")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"