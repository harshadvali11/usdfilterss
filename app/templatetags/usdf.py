from django import template

register=template.Library()

def swap(value):
    return value.swapcase()

def counting(value,sc):
    return value.lower().count(sc.lower())

@register.filter()
def delete(value,dc):
    return value.replace(dc,'')

register.filter('swapping',swap)
register.filter('counting',counting)
