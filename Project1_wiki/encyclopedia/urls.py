from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pageTitle>", views.wikiPage, name="wikipages")
]
