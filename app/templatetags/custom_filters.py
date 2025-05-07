from django import template


# yourapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Retrieve a value from a dictionary using a key."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, 0)
    return 0




from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)



register = template.Library()

@register.filter
def get_dict_value(dictionary, key):
    """Retrieve a value from a dictionary, defaulting to '-' if key is not found."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, "-")
    return "-"

@register.filter
def get_item(dictionary, key):
    """Retrieve a value from a dictionary, defaulting to 0 if key is not found."""
    if isinstance(dictionary, dict):
        return dictionary.get(key, 0)
    return 0

from django import template

register = template.Library()


from django import template

register = template.Library()

@register.filter
def dict_get(d, key):
    return d.get(key, 'N/A')



@register.filter
def get_item(dictionary, key):
    """Custom template filter to get a dictionary value by key."""
    return dictionary.get(key, "N/A")

from django import template

register = template.Library()

@register.filter
def get_dict_value(dictionary, key):
    """Retrieve a value from a dictionary using a key."""
    return dictionary.get(key, "-")  # Default to "-"

@register.filter
def get_item(dictionary, key):
    """Retrieve a value from a dictionary using a key (alternative)."""
    return dictionary.get(key, "-")  # Default to "-"
