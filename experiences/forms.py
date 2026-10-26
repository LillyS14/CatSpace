from django import forms

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


class ExperienceCreateForm(ExperienceBaseForm):
    pass


class ExperienceUpdateForm(ExperienceBaseForm):
    pass
