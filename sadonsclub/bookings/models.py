from django.db import models

MAX_LENGTH_CHARFIELD = 256


class Category(models.Model):
    category_name = models.CharField(
        max_length=MAX_LENGTH_CHARFIELD
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    
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
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.category.category_name
