from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser



# Create your views here.

def ProjectsView(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProjectSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

