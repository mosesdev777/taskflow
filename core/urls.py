# your_project_name/urls.py

from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path("admin/", admin.site.urls),
    # Add this line to include your tasks app URLs
    path("", include("taskflow.urls", namespace="taskflow")),
]
