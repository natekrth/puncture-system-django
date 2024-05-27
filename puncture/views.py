# puncture_system/views.py

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

def index(request):
    context = {}
    # Check if the session has the uploaded image URL
    if 'uploaded_image_url' in request.session:
        context['uploaded_image_url'] = request.session['uploaded_image_url']
        # Remove the URL from the session after reading it
        del request.session['uploaded_image_url']
    return render(request, 'index.html', context)

def upload_image(request):
    if request.method == 'POST' and request.FILES['uploaded_image']:
        uploaded_image = request.FILES['uploaded_image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fs.url(filename)
        # Store the uploaded image URL in the session
        request.session['uploaded_image_url'] = uploaded_image_url
        # Redirect to the index page
        return redirect('index')
    return render(request, 'upload_image.html')
