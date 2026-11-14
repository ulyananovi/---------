from django.shortcuts import render
from .models import Category, Dish, Filter

def catalog_view(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    
    category_id = request.GET.get('category')
    active_category = None
    filters = Filter.objects.none()

    if category_id:
        active_category = Category.objects.filter(id=category_id).first()
        if active_category:
            dishes = dishes.filter(category=active_category)
            filters = active_category.filters.all()

    tag_id = request.GET.get('tag')
    if tag_id:
        dishes = dishes.filter(filters__id=tag_id)

    context = {
        'categories': categories,
        'dishes': dishes,
        'filters': filters,
        'active_category': active_category,
        'current_tag': int(tag_id) if tag_id else None,
    }
    return render(request, 'pages/catalog.html', context)