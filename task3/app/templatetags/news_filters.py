from django import template
from datetime import datetime
import time

register = template.Library()


@register.filter
def format_date(value):
    time_difference = int(time.time()) - int(value)
    if (time_difference < 600) and (time_difference >= 0.001):
        return 'just now'
    elif (time_difference < 86400) and (time_difference >= 600):
        hours_ago = time_difference // 3600
        if hours_ago == 0:
            return "больше 10 минут, но меньше часа назад"
        return f'{hours_ago} часов назад '
    else:
        return time.ctime(value)


# необходимо добавить фильтр для поля `score`

@register.filter
def score(value):
    if value < -5:
        return 'все плохо'
    elif (value >= -5) and (value <= 5):
        return 'нейтрально'
    else:
        return 'хорошо'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif (value > 0) and (value <= 50):
        return f'{value}'
    else:
        return '50+'


@register.filter
def format_selftext(value: str, count_of_words: int):
    list_of_words = value.split(' ')
    reversed_list = list_of_words[::-1]
    if reversed_list != None:
        if len(list_of_words) > 2 * count_of_words:
            first_part = ' '.join(list_of_words[0:count_of_words])
            second_part = ' '.join(reversed_list[0:count_of_words])
            return first_part + '...' + second_part
        else:
            return ''.join(list_of_words)
    else:
        return ''
