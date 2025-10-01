from django.contrib import admin
from .models import ImageUpload

# Register your models here.
@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'original', 'processed', 'uploaded_at')