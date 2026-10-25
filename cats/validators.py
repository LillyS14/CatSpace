from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_birthday(value):
    if value and value > timezone.localdate():
        raise ValidationError("Birthday cannot be in the future")
