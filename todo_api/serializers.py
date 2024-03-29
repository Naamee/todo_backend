from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']
        
class TaskSerializer(serializers.ModelSerializer):
    due_date = serializers.DateField(input_formats=['%d/%m/%Y'], format='%d/%m/%Y')

    class Meta:
        model = Task
        fields = ['id', 'project', 'title', 'description', 'due_date', 'priority', 'completed']
