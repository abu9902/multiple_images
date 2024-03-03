
from django.shortcuts import render, redirect
from .models import *


def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        images = request.FILES.getlist('images')  # Access files from request.FILES
        
        project = Project.objects.create(title=title, description=description)

        # Loop through each uploaded image and save it along with the project
        for img in images:
            ProjectImage.objects.create(project=project, image=img)

        return redirect('index')  # Redirect to the appropriate URL after saving
    return render(request, 'app/create.html')  # Correct the template path



def index(request):  
    projects = Project.objects.all()
    context ={
        "projects":projects,
        }
    return render(request,'app/index.html', context)
