from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("index/?q=<str:query>", views.search, name="search"),
    path("<str:name>", views.entry, name="entry")
]
