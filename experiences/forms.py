from django import forms
from django.core.exceptions import ValidationError

from catspace.mixins import StyledFormMixin
from experiences.models import Experience


class ExperienceBaseForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ["slug"]
        widgets = {
            "cover_image_url": forms.URLInput(attrs={"placeholder": "https://example.com"})
        }
        labels = {"cover_image_url": "Cover image URL"}

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("teammate") and cleaned_data.get("is_available"):
            raise ValidationError("A leading teammate is required for an available experience.")
        return cleaned_data


class ExperienceCreateForm(ExperienceBaseForm):
    pass


class ExperienceUpdateForm(ExperienceBaseForm):
    pass
