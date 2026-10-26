from django.db import models
from django import forms


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StyledFormMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.required:
                field.label += "*"
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({"class": "form-control"})
