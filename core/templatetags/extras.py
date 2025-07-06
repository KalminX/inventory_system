# yourapp/templatetags/extras.py
from django import template

register = template.Library()

@register.filter
def get_field_names(obj):
    return [f.name for f in obj.__class__._meta.fields if f.name != 'id']

@register.filter
def get_field_value(obj, field_name):
    return getattr(obj, field_name)
