from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name="Картинка")

    def __str__(self):
        return self.name

class Filter(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название фильтра (например, С мясом)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='filters', verbose_name="Категория")

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Dish(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название блюда")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    weight = models.CharField(max_length=50, blank=True, verbose_name="Вес/Объем")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Картинка")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name="Категория")
    
    filters = models.ManyToManyField(Filter, blank=True, verbose_name="Теги/Фильтры")

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Блюдо")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    status = models.CharField(max_length=50, default='Новый', verbose_name="Статус")

    def __str__(self):
        return f"{self.user.username} - {self.dish.title}"