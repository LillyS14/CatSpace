from django.urls import path, include

from . import  views


app_name = "experiences"

urlpatterns = [
        path("", views.ExperienceList.as_view(), name="list"),
        path("create/", views.CreateExperience.as_view(), name="create"),
        path("<slug:slug>/", include([
            path("", views.ExperienceDetail.as_view(), name="detail"),
            path("update/", views.UpdateExperience.as_view(), name="update"),
            path("delete/", views.DeleteExperience.as_view(), name="delete"),
        ]))
]