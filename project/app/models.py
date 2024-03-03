from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    # Other fields...

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
