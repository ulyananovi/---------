from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Dish(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название блюда")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена")
    weight = models.CharField(max_length=50, blank=True, verbose_name="Вес/Объем")
    image_name = models.CharField(max_length=100, blank=True, verbose_name="Имя файла картинки")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes', verbose_name="Категория")

    def __str__(self):
        return self.title