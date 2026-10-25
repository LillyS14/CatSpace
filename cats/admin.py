from django.contrib import admin

from cats.models import Cat


# Register your models here.
@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass
