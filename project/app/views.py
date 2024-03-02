from django.shortcuts import render, redirect
from .models import Multiple

def index(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for image in images:
            Multiple.objects.create(images=image)
        return redirect('index')  # Redirect to the same page to avoid resubmission
    else:
        images = Multiple.objects.filter(images__icontains='.jpg') | \
                 Multiple.objects.filter(images__icontains='.jpeg') | \
                 Multiple.objects.filter(images__icontains='.png') | \
                 Multiple.objects.filter(images__icontains='.gif')
        
        videos = Multiple.objects.exclude(images__icontains='.jpg').exclude(images__icontains='.jpeg').exclude(images__icontains='.png').exclude(images__icontains='.gif')
        
        return render(request, 'app/index.html', {'uploaded_images': images, 'uploaded_videos': videos})
