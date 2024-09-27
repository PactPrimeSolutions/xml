# editor/custom_filters.py
from django import template

register = template.Library()

@register.filter
def pretty_key(key):
    """Convert a key from snake_case to Title Case."""
    return key.replace('_', ' ').title()
