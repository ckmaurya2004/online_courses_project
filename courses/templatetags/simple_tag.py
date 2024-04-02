from django import template
import math

register = template.Library()

@register.filter(name='cal_selprice')
def cal_selprice(price,disount):
    selprice = price
    selprice = price-(price*disount*0.01)
    if selprice == 0:
        return  math.floor(selprice)
    return math.floor(selprice)



@register.filter(name='zero_cal_selprice')
def zero_cal_selprice(price,disount):
    selprice = price
    selprice = price-(price*disount*0.01)
    if selprice == 0:
        return  False
    return True