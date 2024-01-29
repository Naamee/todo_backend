from django.shortcuts import render
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework import mixins


# Create your views here.
class ProjectViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer