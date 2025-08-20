# tasks/models.py

from django.db import models
from django.conf import settings


# Create your models here.
class Task(models.Model):
    """
    Represents a single task in the to-do list application.
    Each task has a title, description, status, and is associated with a specific user.
    """

    class Status(models.TextChoices):
        """
        Enumeration for the status of a task.
        Provides choices for the status field.
        """

        PENDING = "PENDIENTE", "Pendiente"
        IN_PROGRESS = "EN_PROGRESO", "En Progreso"
        COMPLETED = "COMPLETADA", "Completada"

  
    title = models.CharField(max_length=200, verbose_name="Título")  #
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")  #
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Estado",
    )  #
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )  #
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización"
    )  #

    class Meta:
        """
        Meta options for the Task model.
        """

        ordering = ["-created_at"]  # Orders tasks by creation date, newest first.
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        """
        String representation of the Task model.
        Returns the title of the task.
        """
        return self.title
