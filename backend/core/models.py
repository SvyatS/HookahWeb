from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class ExtendedUser(models.Model):
    """Класс который расширяет стандартный класс юзера"""

    _status_choices = [
        ("Администратор", "admin"),
        ("Сотрудник", "staff"),
        ("Клиент", "user")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length = 64, choices = _status_choices, default = "Клиент")


class Table(models.Model):
    """Модель записи стола"""

    _status_choices = [
        ("Свободен", "free"),
        ("Занят", "reserve"),
    ]

    max_people = models.IntegerField("Количество человек", default = 4)
    status = models.CharField(max_length = 32, choices = _status_choices, default = "Свободен")
    x_pos = models.IntegerField("X", default = 100, validators=[
            MaxValueValidator(1000),
            MinValueValidator(1)
        ])
    y_pos = models.IntegerField("Y", default = 100, validators=[
            MaxValueValidator(470),
            MinValueValidator(1)
        ])


class Reserve(models.Model):
    """Бронирование столиков"""

    number_of_users = models.IntegerField("Количество человек")
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    order_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField("Забронированное время")


class Review(models.Model):
    """Модель отзывов"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Отзыв")
    date = models.DateField("Дата создания", auto_now_add = True)


class Product(models.Model):
    """Модель товаров"""

    name = models.CharField("Имя товара", max_length=64)
    price = models.IntegerField("Цена товара")
    photo = models.FileField("Фото товара", upload_to="media/")
