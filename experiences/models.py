from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from catspace.mixins import TimeStampMixin


# Create your models here.
class Experience(TimeStampMixin):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    cover_image_url = models.URLField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)])
    teammate = models.ForeignKey("teammates.Teammate", on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="experiences")
    is_available = models.BooleanField(default=True, blank=True)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ["-updated_at"]

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        new_slug = slugify(f"{self.name}-{self.pk}")
        if self.slug != new_slug:
            self.slug = new_slug
            super().save(update_fields=["slug"])

    def __str__(self) -> str:
        return self.name
