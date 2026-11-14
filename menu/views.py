from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Dish

def catalog_view(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    
    category_id = request.GET.get('category')
    if category_id:
        dishes = dishes.filter(category_id=category_id)

    tag = request.GET.get('tag')
    if tag:
        dishes = dishes.filter(filters__icontains=tag)

    context = {
        'categories': categories,
        'dishes': dishes,
        'current_tag': tag,
    }
    return render(request, 'pages/catalog.html', context)