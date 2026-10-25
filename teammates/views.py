from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from teammates.models import Teammate


# Create your views here.
class TeammateList(ListView):
    model = Teammate


class CreateTeammate(CreateView):
    model = Teammate
    fields = "__all__"
    success_url = reverse_lazy("teammates:list")
    template_name = "common/form.html"


class TeammateDetail(DetailView):
    queryset = Teammate.objects.prefetch_related("experiences")


class UpdateTeammate(UpdateView):
    model = Teammate
    fields = "__all__"
    success_url = reverse_lazy("teammates:list")
    template_name = "common/form.html"


class DeleteTeammate(DeleteView):
    model = Teammate
    success_url = reverse_lazy("teammates:list")
    template_name = "common/confirm_delete.html"
