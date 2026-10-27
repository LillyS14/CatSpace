from django import forms
from django.core.exceptions import ValidationError

from catspace.mixins import StyledFormMixin
from teammates.models import Teammate


class TeammateBaseForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Teammate
        fields = "__all__"
        labels = {"image_url": "Image URL"}
        widgets = {
            "description": forms.Textarea(attrs={"placeholder": "e.g., skills, experience, hobbies, values, dreams"}),
            "image_url": forms.URLInput(attrs={"placeholder": "https://example.com"}),
        }
        error_messages = {
            "phone": {
                "invalid": "Enter a valid phone number (e.g. 0883 555 555) or a number with an international call prefix."}
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(char.isdigit() for char in name):
            raise ValidationError("Please enter a valid name without numbers")
        return name.strip()
