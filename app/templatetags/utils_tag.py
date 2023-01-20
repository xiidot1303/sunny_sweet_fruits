from django import template
from app.utils import *

register = template.Library()

@register.filter()
def index(l, i):
    return l[i]

@register.filter()
def three_elements(obj):
    return obj[:3]