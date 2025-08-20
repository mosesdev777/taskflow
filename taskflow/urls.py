# tasks/urls.py

from django.urls import path
from . import views

# This is crucial for namespacing URLs.
# It allows us to use names like 'tasks:list' in our templates.
app_name = "tasksflow"

urlpatterns = [
    # Example: /tasks/
    path("", views.TaskListView.as_view(), name="list"),
    # Example: /tasks/5/
    path("<int:pk>/", views.TaskDetailView.as_view(), name="detail"),
    # Example: /tasks/create/
    path("create/", views.TaskCreateView.as_view(), name="create"),
    # Example: /tasks/5/update/
    path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="update"),
    # Example: /tasks/5/delete/
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="delete"),
]
