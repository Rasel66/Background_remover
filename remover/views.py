import os
from django.shortcuts import render, redirect
from django.conf import settings
from rembg import remove
from PIL import Image
from .forms import ImageUploadForm
from .models import ImageUpload

# Create your views here.

def upload_image_view(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            input_image = Image.open(instance.original)
            output_image = remove(input_image)

            processed_path = os.path.join(settings.MEDIA_ROOT, 'processed', os.path.basename(instance.original.name))
            os.makedirs(os.path.dirname(processed_path), exist_ok=True)
            output_image.save(processed_path, format='PNG')

            instance.processed.name = f'processed/{os.path.basename(instance.original.name)}'
            instance.save()

            return redirect('result', pk=instance.pk)
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})


def result_view(request, pk):
    image = ImageUpload.objects.get(id=pk)
    context = {
        'original_url': image.original.url,
        'processed_url': image.processed.url
    }
    return render(request, 'result.html', context)