from django.urls import path, include

from . import views


app_name = "memories"

urlpatterns = [
    path("", views.MemoryList.as_view(), name="list"),
    path("create/", views.CreateMemory.as_view(), name="create"),
    path("<int:pk>/", include([
        path("", views.MemoryDetail.as_view(), name="detail"),
        path("update/", views.UpdateMemory.as_view(), name="update"),
        path("delete/", views.DeleteMemory.as_view(), name="delete"),
    ]))
]
