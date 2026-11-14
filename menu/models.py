from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    image_name = models.CharField(max_length=100, blank=True, verbose_name="Имя файла картинки")

    def __str__(self):
        return self.name

class Dish(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название блюда")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    weight = models.CharField(max_length=50, blank=True, verbose_name="Вес/Объем")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Картинка")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name="Категория")

    filters = models.CharField(max_length=200, blank=True, verbose_name="Теги (через запятую)")

    def __str__(self):
        return self.title