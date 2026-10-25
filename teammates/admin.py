from django.contrib import admin

from teammates.models import Teammate


# Register your models here.
@admin.register(Teammate)
class TeammateAdmin(admin.ModelAdmin):
    pass

