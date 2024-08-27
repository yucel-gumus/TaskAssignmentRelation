from django.urls import path
from .views import task_frequencies_view

urlpatterns = [
    path('task-frequencies/', task_frequencies_view, name='task_frequencies'),
]
