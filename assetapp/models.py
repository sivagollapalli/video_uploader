from django.db import models

# Create your models here.
class Asset(models.Model):
  file_name = models.CharField(max_length=255, blank=True)
  document = models.FileField(upload_to='uploads/')
  uploaded_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)