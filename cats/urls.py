from django.urls import path, include
from . import views

app_name = "cats"

urlpatterns = [
        path("", views.CatList.as_view(), name="list"),
        path("create/", views.CreateCat.as_view(), name="create"),
        path("<int:pk>/", include([
            path("", views.CatDetail.as_view(), name="detail"),
            path("update/", views.UpdateCat.as_view(), name="update"),
            path("delete/", views.DeleteCat.as_view(), name="delete"),
        ]))
]
