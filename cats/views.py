from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from cats.forms import CatCreateForm, CatUpdateForm
from cats.models import Cat


# Create your views here.
class CatList(ListView):
    paginate_by = 6

    def get_queryset(self):
        queryset = Cat.objects.prefetch_related("memories")

        q = self.request.GET.get("query", "").strip()
        e = self.request.GET.get("eyes")
        f = self.request.GET.get("fur")

        if q:
            queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        if e:
            queryset = queryset.filter(eyes=e)
        if f:
            queryset = queryset.filter(fur=f)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["eye_choices"] = Cat.objects.values_list("eyes", flat=True).distinct().order_by("eyes")
        context["fur_choices"] = Cat.objects.values_list("fur", flat=True).distinct().order_by("fur")
        return context


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
