from django import template
from menu.models import Menu
register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    active_url = context['request'].path_info
    menu = Menu.objects.select_related("parent").get(name=menu_name)
    return {
        "active_url": active_url,
        "menu": menu,
    }