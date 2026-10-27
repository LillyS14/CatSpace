from django.db.models import Avg, Q
from django.views.generic import TemplateView

from cats.models import Cat
from experiences.models import Experience
from memories.models import Memory


class Home(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["first_cat"] = Cat.objects.first()
        context["recent_top_memories"] = Memory.objects.filter(Q(rating__gte=8) | Q(rating__isnull=True))[:2]
        context["latest_top_experiences"] = Experience.objects.select_related("teammate").annotate(
            avg_rating=Avg("memories__rating")).filter(Q(avg_rating__gte=8) | Q(avg_rating__isnull=True),
                                                       is_available=True).order_by("-updated_at")[:2]
        return context


class Contact(TemplateView):
    template_name = "common/contact.html"
