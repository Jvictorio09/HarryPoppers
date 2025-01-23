from django import template
from django.forms.boundfield import BoundField

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    if isinstance(field, BoundField):  # Ensure it's a valid form field
        return field.as_widget(attrs={"class": css_class})
    return field  # Return the original field if it's not a form field
