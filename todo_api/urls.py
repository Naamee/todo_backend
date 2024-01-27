from django.urls import path
from .views import project_list, task_list, project_detail, task_detail

urlpatterns = [
    path('projects/', project_list),
    path('tasks/', task_list),
    path('projects/<int:pk>/', project_detail),
    path('tasks/<int:pk>/', task_detail),
]