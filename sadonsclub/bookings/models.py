from django.db import models

from datetime import timedelta

MAX_LENGTH_CHARFIELD = 256


class Category(models.Model):
    category_name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class Computers(models.Model):
    booking = models.BooleanField(
        default=False,
        verbose_name='Забронирован'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Рабочий'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='category'
    )

    class Meta:
        verbose_name = 'компьютер'
        verbose_name_plural = 'Компьютеры'

    def __str__(self):
        return f'{self.category.category_name} №{self.pk}'


class Bookings(models.Model):
    computer_id = models.ForeignKey(
        Computers,
        null=True,
        on_delete=models.SET_NULL
    )
    username = models.ForeignKey(
        'users.CustomUsers',
        null=True,
        on_delete=models.SET_NULL
    )
    booking_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время бронирования'
    )
    booked_from = models.TimeField(
        verbose_name='Дата начала бронирования'
    )
    booked_until = models.TimeField(
        verbose_name='Дата окончания бронирования'
    )
    booked_to_date = models.DateField(
        verbose_name='Дата предстоящего бронирования'
    )
    status = models.BooleanField(
        default=True,
        verbose_name='Статус'
    )

    class Meta:
        verbose_name  = 'бронирование'
        verbose_name_plural = 'Бронирования'
    
    def __str__(self):
        return f'{self.pk}'