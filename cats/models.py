from django.db import models
from django.utils import timezone

from cats.validators import validate_birthday
from catspace.mixins import TimeStampMixin


# Create your models here.
class Cat(TimeStampMixin):
    class FurChoice(models.TextChoices):
        BLACK = "Black", "Black"
        WHITE = "White", "White"
        GINGER = "Ginger", "Ginger"
        GRAY = "Gray", "Gray"
        TABBY = "Tabby", "Tabby"
        TUXEDO= "Tuxedo", "Tuxedo"
        CALICO = "Calico", "Calico"
        OTHER = "Other", "Other"

    class EyesChoice(models.TextChoices):
        BLUE = "Blue", "Blue"
        GREEN = "Green", "Green"
        YELLOW = "Yellow", "Yellow"
        ORANGE = "Orange", "Orange"
        HETEROCHROMIA = "Heterochromia", "Heterochromia"
        OTHER = "Other", "Other"

    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True, validators=[validate_birthday])
    image_url = models.URLField(blank=True, null=True)
    eyes = models.CharField(choices=EyesChoice.choices, max_length=20)
    fur = models.CharField(choices=FurChoice.choices, max_length=20)
    is_long_haired = models.BooleanField(default=False, blank=True)

    @property
    def age(self) -> int | None:
        if self.birthday:
            today = timezone.localdate()
            return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return None

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["created_at"]
