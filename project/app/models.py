from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

def validate_file_size(value):
    max_file_size = 200 * 1024 * 1024
    if value.size > max_file_size:
        raise ValidationError(f"File hajmi {max_file_size / (1024 * 1024)} mb dan kichik bolishi kerak!")



class Video(models.Model):
    video = models.FileField(upload_to='video/' , validators=[FileExtensionValidator(allowed_extensions=['mp4','mkv','avi','mov']),validate_file_size])
    created = models.DateTimeField(auto_now_add=True )
    description = models.TextField()


    def __str__(self):
        return self.video