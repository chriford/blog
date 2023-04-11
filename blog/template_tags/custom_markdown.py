from django import template
from django.template.defaultfilters import stringfilter

from markdown import markdown

register = template.Library()


@register.filter(name="convert_markdown")
def convert_markdown(value):
    converted_value = markdown(value)
    return converted_value
