from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from cats.forms import CatCreateForm, CatUpdateForm
from cats.models import Cat


# Create your views here.
class CatList(ListView):
    queryset = Cat.objects.prefetch_related("memories")
    paginate_by = 6


class CreateCat(CreateView):
    model = Cat
    form_class = CatCreateForm
    success_url = reverse_lazy("cats:list")
    template_name = "common/form.html"


class CatDetail(DetailView):
    queryset = Cat.objects.prefetch_related("memories")


class UpdateCat(UpdateView):
    model = Cat
    form_class = CatUpdateForm
    success_url = reverse_lazy("cats:list")
    template_name = "common/form.html"


class DeleteCat(DeleteView):
    model = Cat
    success_url = reverse_lazy("cats:list")
    template_name = "common/confirm_delete.html"
