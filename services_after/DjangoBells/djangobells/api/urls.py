from django.urls import path

from . import views

urlpatterns = [

    path("read/<str:post_id>/<str:pass_token>/read", views.read, name="read"),
    path("read/<str:post_id>/<str:pass_token>/edit", views.edit, name="edit"),
    path("report/", views.report, name="report"),
    path("list/", views.list, name="list"),
    path("create/", views.create, name="create")
]
