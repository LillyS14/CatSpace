from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.contrib import messages

from memories.forms import MemoryCreateForm, MemoryUpdateForm, MemoryDeleteForm
from memories.models import Memory


# Create your views here.
class MemoryList(ListView):
    queryset = Memory.objects.select_related("experience").prefetch_related("cats")
    paginate_by = 3


class CreateMemory(CreateView):
    model = Memory
    form_class = MemoryCreateForm
    template_name = "common/form.html"
    success_url = reverse_lazy("memories:list")

    def form_valid(self, form):
        messages.success(self.request, "Memory added successfully.")
        return super().form_valid(form)


class MemoryDetail(DetailView):
    queryset = Memory.objects.select_related("experience").prefetch_related("cats")


class UpdateMemory(UpdateView):
    model = Memory
    form_class = MemoryUpdateForm
    success_url = reverse_lazy("memories:list")
    template_name = "common/form.html"

    def form_valid(self, form):
        messages.success(self.request, f"Memory {self.object} updated successfully.")
        return super().form_valid(form)


class DeleteMemory(DeleteView):
    model = Memory
    success_url = reverse_lazy("memories:list")
    template_name = "memories/memory_delete_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MemoryDeleteForm(instance=self.object)
        return context
