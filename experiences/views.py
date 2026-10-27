from django.db.models import Avg, Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from experiences.forms import ExperienceCreateForm, ExperienceUpdateForm
from experiences.models import Experience


# Create your views here.
class ExperienceList(ListView):
    paginate_by = 6

    def get_queryset(self):
        queryset = (Experience.objects.filter(is_available=True).select_related("teammate").prefetch_related("memories")
                    .annotate(avg_rating=Avg("memories__rating")).order_by("-updated_at"))

        q = self.request.GET.get("query")

        if q:
            q = q.strip()
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(description__icontains=q) | Q(teammate__name__icontains=q))

        return queryset


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
