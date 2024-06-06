from django import template

register = template.Library()

@register.filter(name='range')
def range_filter(value):
    return range(value)


@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return value * arg
    except:
        return None