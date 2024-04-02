
from django import template


register = template.Library()

@register.filter(name='currency_filter')
def currency_filter(price):
    return "₹ " + str(price)