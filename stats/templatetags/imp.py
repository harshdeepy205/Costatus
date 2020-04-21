from django import template

register = template.Library()

@register.filter(name='value')
def value(lists,i):
    a=i-1
    return lists[a]