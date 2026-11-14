from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render, redirect
from .models import Category, Dish, Filter, Order
from django.http import JsonResponse
import json

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

def make_order(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'status': 'error', 'message': 'Необходимо войти в аккаунт'}, status=401)
        
        try:
            data = json.loads(request.body)
            dish_id = data.get('dish_id')
            dish = Dish.objects.get(id=dish_id)
            
            Order.objects.create(user=request.user, dish=dish)
            return JsonResponse({'status': 'success', 'message': 'Заказ успешно создан'})
        except Dish.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Блюдо не найдено'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
            
    return JsonResponse({'status': 'error', 'message': 'Метод не разрешен'}, status=405)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.first_name = form.cleaned_data.get('full_name')
            user.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('catalog')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')