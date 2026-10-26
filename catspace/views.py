from django.views.generic import TemplateView

from cats.models import Cat


class Home(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = Cat.objects.first()
        return context

class Contact(TemplateView):
    template_name = "common/contact.html"
