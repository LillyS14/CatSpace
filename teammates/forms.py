from django import forms

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
