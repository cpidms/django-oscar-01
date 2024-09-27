import pathlib
import uuid
from django.db import models


def image_file_upload_handler(instance, filepath):
    instance_id = instance.id
    if not instance.id:
        instance_id = "0"
    filepath = pathlib.Path(filepath).resolve()
    fname = str(uuid.uuid1())
    ext = filepath.suffix
    return f"blog/{instance_id}/{fname}/{filepath.name}"

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content  = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=image_file_upload_handler, blank=True, null=True)

