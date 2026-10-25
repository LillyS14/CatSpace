from django import forms

from experiences.models import Experience


class ExperienceBaseForm(forms.ModelForm):
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
