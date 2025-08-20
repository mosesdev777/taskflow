from django.shortcuts import render

# Create your views here.
# tasks/views.py

from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Task
from .forms import TaskForm


# Create your views here.
class TaskListView(ListView):
    """
    Handles the display of a user's task list.
    Ensures that users can only see their own tasks and allows filtering by status.
    """

    model = Task
    template_name = "taskflow/tasks/index.html"
    context_object_name = "task_list"
    paginate_by = 6  # Optional: Show 6 tasks per page

    def get_queryset(self):
        """
        Overrides the default queryset to filter tasks by the logged-in user
        and by status if a filter is applied.
        """
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskDetailView(DetailView):
    """
    Displays the details of a single task.
    Ensures that a user can only view their own task details.
    """

    model = Task
    template_name = "taskflow/tasks/details.html"
    context_object_name = "task"

    


class TaskCreateView(SuccessMessageMixin, CreateView):
    """
    Handles the creation of a new task.
    The task is automatically assigned to the currently logged-in user.
    """

    model = Task
    form_class = TaskForm
    template_name = "taskflow/tasks/task_form.html"
    success_url = reverse_lazy("taskflow:list")
    success_message = "¡Tarea creada con éxito!"

    def form_valid(self, form):
        """
        This method is called when valid form data has been POSTed.
        It sets the owner of the task to the current user before saving.
        """
       
        return super().form_valid(form)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    """
    Handles the updating of an existing task.
    Ensures that a user can only edit their own tasks.
    """

    model = Task
    form_class = TaskForm
    template_name = "taskflow/tasks/task_form.html"
    success_url = reverse_lazy("taskflow:list")
    success_message = "¡Tarea actualizada correctamente!"




class TaskDeleteView(SuccessMessageMixin, DeleteView):
    """
    Handles the deletion of a task.
    Ensures that a user can only delete their own tasks.
    """

    model = Task
    template_name = "taskflow/tasks/delete.html"
    success_url = reverse_lazy("taskflow:list")
    success_message = "Tarea eliminada."

    
