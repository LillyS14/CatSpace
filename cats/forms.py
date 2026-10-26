from django import forms

from cats.models import Cat
from catspace.mixins import StyledFormMixin


class CatBaseForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Cat
        fields = "__all__"
        widgets = {
            "description": forms.Textarea(attrs={"placeholder": "e.g., playful, cuddly, sassy, calm, adorable kitten "}),
            "birthday": forms.DateInput(attrs={"type": "date"}),
            "image_url": forms.URLInput(attrs={"placeholder": "https://example.com"})
        }
        labels = {"image_url": "Image URL"}
        error_messages = {
            "name": {"unique": "We already have a cat with the same name 🐾"}
        }


class CatCreateForm(CatBaseForm):
    pass


class CatUpdateForm(CatBaseForm):
    pass
