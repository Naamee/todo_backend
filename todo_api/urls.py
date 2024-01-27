from django.urls import path
from .views import ProjectsView, TaskView

urlpatterns = [
    path('projects/', ProjectsView),
    path('tasks/', TaskView),
]