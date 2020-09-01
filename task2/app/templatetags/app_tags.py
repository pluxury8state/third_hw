from django import template


register = template.Library()


@register.filter
def isclass(value: str, li_value):
    if li_value == 1:
        li_value = '/examples/'
    elif li_value == 2:
        li_value = '/contacts/'
    elif li_value == 3:
        li_value = '/about/'

    if value == li_value:
        return 'class=active'
    return None

