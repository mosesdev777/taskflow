# tasks/forms.py

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    A ModelForm for creating and updating Task instances.
    It includes fields for title, description, and status, with Tailwind CSS classes
    applied to the widgets for styling.
    """

    class Meta:
        """
        Meta options for the TaskForm.
        """

        model = Task
        fields = ["title", "description", "status"]

    def __init__(self, *args, **kwargs):
        """
        Overrides the init method to add Tailwind CSS classes to the form fields.
        """
        super().__init__(*args, **kwargs)

        # Common classes for all input fields to ensure a consistent look and feel.
        common_classes = (
            "w-full px-3 py-2 mt-1 "
            "text-gray-900 dark:text-gray-100 "
            "bg-white dark:bg-gray-800 "
            "border border-gray-300 dark:border-gray-600 "
            "rounded-md shadow-sm "
            "focus:outline-none focus:ring-2 "
            "focus:ring-indigo-400 dark:focus:ring-indigo-400"  # Using the 'Info' color from your palette for focus
        )

        # Apply the common classes to all fields in the form.
        self.fields["title"].widget.attrs.update({"class": common_classes})
        self.fields["description"].widget.attrs.update(
            {"class": f"{common_classes} h-32"}
        )  # Add extra height for textarea
        self.fields["status"].widget.attrs.update({"class": common_classes})
