from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Dish
from .forms import DishForm

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

def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = DishForm()
    return render(request, 'pages/add_dish.html', {'form': form})

def edit_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = DishForm(instance=dish)
    return render(request, 'pages/edit_dish.html', {'form': form, 'dish': dish})

def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        dish.delete()
        return redirect('catalog')
    return render(request, 'pages/delete_dish.html', {'dish': dish})