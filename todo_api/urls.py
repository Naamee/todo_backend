from django.urls import path, include
from .views import ProjectViewSet, TaskViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
]