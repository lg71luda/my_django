
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

app_name = "todo_list"

urlpatterns = [
    # path("", views.index_view, name="index"),
    # path("", views.ToDoListIndexView.as_view(), name="index"),
    path("", views.ToDoListIndexView.as_view(), name="index"),
    path("<int:pk>/", views.ToDoDetailView.as_view(), name="detail"),
    path("list/", views.ToDoListView.as_view(), name="list"),
    path("done/", views.ToDoListDoneView.as_view(), name="done"),
]
