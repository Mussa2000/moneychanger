# ordinal_filter.py
from django import template
import inflect

register = template.Library()

@register.filter(name="ordinal")
def ordinal(value):
    inflect_engine = inflect.engine()
    return inflect_engine.ordinal(value)
