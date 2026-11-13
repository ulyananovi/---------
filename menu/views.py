from django.shortcuts import render
from .models import Category, Dish

def catalog_view(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    
    category_id = request.GET.get('category')
    if category_id:
        dishes = dishes.filter(category_id=category_id)

    context = {
        'categories': categories,
        'dishes': dishes,
    }
    return render(request, 'pages/catalog.html', context)