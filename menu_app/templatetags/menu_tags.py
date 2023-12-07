from django import template
from menu_app.models import Menu, MenuItem
from menu_app.utils import build_menu_tree

register = template.Library()

@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = Menu.objects.get(name=menu_name)
    items = menu.items.all()
    menu_tree = build_menu_tree(items)
    return {'menu_tree': menu_tree, 'request': context['request']}
