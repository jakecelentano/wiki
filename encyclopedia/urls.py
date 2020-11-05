from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("<str:name>", views.entry, name="entry"),
    path("new/", views.new, name="new"),
    path("random/", views.randomPage, name="random"),
    path("edit/", views.edit, name="edit")
  
]
