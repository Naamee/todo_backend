from django.urls import path
from .views import ProjectsView

urlpatterns = [
    path('projects/', ProjectsView),
]