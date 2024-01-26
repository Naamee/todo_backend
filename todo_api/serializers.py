from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    
    def create(self, validated_data):
        return Project.objects.create(**validated_data)