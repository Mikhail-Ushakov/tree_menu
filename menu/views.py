from django.shortcuts import render
from .models import MenuItem, Menu


def index(request):
    """
    Представление отрисовывает список всех меню с ссылками
    на первый уровень элементов меню
    """
    list_menu = Menu.objects.all()
    context = {
        'list_menu': list_menu,
    }
    return render(request, 'menu/index.html', context)

def draw_menu(request, name_menu, url_item):
    """
    Представление отрисовывает страницу с конкретным меню
    """
    context = {
        'name_menu': name_menu, 
        'url_item': url_item,
    }
    return render(request, 'menu/menu.html', context)