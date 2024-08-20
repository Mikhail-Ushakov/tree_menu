from django import template
from menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/menu_tags/draw_menu.html')
def draw_menu(name_menu, url_item):
    """
    Формируем контекст для передачи в шаблон.
    Для выбранного элемента загружается цепочка родителей
    и первый уровень дочерних элементов
    """
    menu_items = MenuItem.objects.filter(menu__name=name_menu)
    item = menu_items.get(url=url_item)
    chain_items_list = []
    while item:
        chain_items_list.append(item.id)
        item = item.parent

    menu_items_values = menu_items.values()
    main_parents = [item for item in menu_items_values.filter(parent=None)]
    for parent in main_parents:
        if parent['id'] in chain_items_list:
            parent['child_items'] = get_child_items(
                parent['id'], menu_items_values, chain_items_list
            )
    context = {
        'name_menu': name_menu, 
        'menu_items': main_parents,
    }
    return context


def get_child_items(parent_id, menu_items_values, chain_items_list):
    """
    Функция рекурсивно извлекает список дочерних элементов.
    """
    parent_child_list = [
        item for item in menu_items_values.filter(parent_id=parent_id)
    ]
    for child in parent_child_list:
        if child['id'] in chain_items_list:
            child['child_items'] = get_child_items(
                child['id'], menu_items_values, chain_items_list
            )
    return parent_child_list