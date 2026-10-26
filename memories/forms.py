from django import forms

from catspace.mixins import StyledFormMixin
from memories.models import Memory


class MemoryBaseForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Memory
        fields = "__all__"
        help_texts = {
            "rating": "on a scale of 1 to 10",
        }
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter your comment"}),
            "author": forms.TextInput(attrs={"placeholder": "Enter your name"}),
        }


class MemoryCreateForm(MemoryBaseForm):
    pass


class MemoryUpdateForm(MemoryBaseForm):
    pass


class MemoryDeleteForm(MemoryBaseForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
