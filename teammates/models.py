from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from catspace.mixins import TimeStampMixin


# Create your models here.
class Teammate(TimeStampMixin):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = PhoneNumberField(region="BG", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    username = models.CharField(max_length=30, unique=True, validators=[RegexValidator(r"^\w+\Z")])

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["created_at"]
