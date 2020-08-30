from django.template import library

register = library.Library()


@register.filter
def get_item(some_dict: dict, key: str):
    return some_dict.get(key)

@register.filter
def from_str_to_float(string: str):
    try:
        new_value = float(string)
    except Exception as e:
        return '-'
    else:
        return new_value



@register.filter
def change_color(value):
    try:
        if value < 0:
            return '#0f7004'
        elif (value >= 1) and (value < 2):
            return '#fbc8c9'
        elif (value >= 2) and (value < 5):
            return '#f6767a'
        elif value >= 5:
            return '#fb0008'
        else:
            return 'white'
    except TypeError as e:
        return 'white'


@register.filter
def not_equal(value):
    if value != 'Суммарная':
        return True

    return False