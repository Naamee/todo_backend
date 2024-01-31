from django.shortcuts import render
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response  


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

    @action(detail=False, methods=['get'])
    def get_project_id(self, request):
        project_name = request.query_params.get('name', None)

        if project_name is None:
            return Response({'error': 'Please provide a name parameter'}, status=400)

        try:
            project = Project.objects.get(name=project_name)
            return Response({'project_id': project.id})
        except Project.DoesNotExist:
            return Response({'error': 'Project not found'}, status=404)


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

    @action(detail=False, methods=['GET'])
    def filter_tasks(self, request):
        project_id = request.query_params.get('project_id', None)
        completed = request.query_params.get('completed', None)

        filters = {}
        if project_id is not None:
            filters['project'] = project_id
        if completed is not None:
            filters['completed'] = completed.lower() == 'true'

        tasks = Task.objects.filter(**filters)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)