from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from catspace.mixins import TimeStampMixin


# Create your models here.
class Memory(TimeStampMixin):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="memories/", null=True, blank=True)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                              null=True, blank=True)
    experience = models.ForeignKey("experiences.Experience", on_delete=models.SET_NULL, related_name="memories",
                                   null=True, blank=True)
    cats = models.ManyToManyField("cats.Cat", related_name="memories", blank=True)

    class Meta:
        ordering = ["updated_at"]

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        return reverse("memories:detail", kwargs={"pk": self.pk})
