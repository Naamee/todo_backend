from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    due_date = models.DateField()

    PRIORITY_CHOICES = [
    ('High Priority', 'High Priority'),
    ('Medium Priority', 'Medium Priority'),
    ('Low Priority', 'Low Priority'),
    ]

    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title