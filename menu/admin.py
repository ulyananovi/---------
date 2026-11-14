from django.contrib import admin
from .models import Category, Dish, Filter

class FilterInline(admin.TabularInline):
    model = Filter
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [FilterInline]

class DishAdmin(admin.ModelAdmin):
    filter_horizontal = ('filters',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Filter)