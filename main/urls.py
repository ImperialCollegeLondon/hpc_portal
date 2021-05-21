from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("create_job/", views.create_job, name="create_job"),
    path("success/<int:job_pk>/", views.success, name="success"),
    path("list_jobs/", views.list_jobs, name="list_jobs"),
    path("delete/<int:job_pk>/", views.delete, name="delete"),
]
