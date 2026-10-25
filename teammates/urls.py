from django.urls import path, include

from . import views

app_name = "teammates"

urlpatterns = [
    path("", views.TeammateList.as_view(), name="list"),
    path("create/", views.CreateTeammate.as_view(), name="create"),
    path("<int:pk>/", include([
        path("", views.TeammateDetail.as_view(), name="detail"),
        path("update/", views.UpdateTeammate.as_view(), name="update"),
        path("delete/", views.DeleteTeammate.as_view(), name="delete"),
    ]))
]
