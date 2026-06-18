from django.db import models

class Basket(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name='Название товара'
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество'
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Цена'
    )

    customer_name = models.CharField(
        max_length=100,
        verbose_name='Имя покупателя'
    )

    note = models.TextField(
        blank=True,
        verbose_name='Комментарий'
    )

    def __str__(self):
        return self.product_name
    

