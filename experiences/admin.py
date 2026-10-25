from django.contrib import admin

from experiences.models import Experience


# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass
