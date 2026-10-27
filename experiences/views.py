from django.db.models import Avg
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from experiences.forms import ExperienceCreateForm, ExperienceUpdateForm
from experiences.models import Experience


# Create your views here.
class ExperienceList(ListView):
    queryset = Experience.objects.filter(is_available=True).prefetch_related("memories").annotate(
        avg_rating=Avg("memories__rating")).order_by("-updated_at")
    paginate_by = 6


class CreateExperience(CreateView):
    model = Experience
    form_class = ExperienceCreateForm
    success_url = reverse_lazy("experiences:list")
    template_name = "common/form.html"


class ExperienceDetail(DetailView):
    queryset = Experience.objects.select_related("teammate").prefetch_related("memories").annotate(
        avg_rating=Avg("memories__rating"))


class UpdateExperience(UpdateView):
    model = Experience
    form_class = ExperienceUpdateForm
    success_url = reverse_lazy("experiences:list")
    template_name = "common/form.html"


class DeleteExperience(DeleteView):
    model = Experience
    success_url = reverse_lazy("experiences:list")
    template_name = "common/confirm_delete.html"
