from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    original = models.ImageField(upload_to='originals/')
    processed = models.ImageField(upload_to='processed/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - {self.original.name}"
    