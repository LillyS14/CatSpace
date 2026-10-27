from django import template


register = template.Library()

@register.filter
def stars(value):
    max_stars = 10
    if not value:
        return "Not rated yet"
    value = round(float(value))
    return "★" * value + "☆" * (max_stars - value)
