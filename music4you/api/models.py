from django.db import models
from pydub import AudioSegment
from os import path
from django.core.validators import FileExtensionValidator


# Create your models here.
class Music(models.Model):
    """This class represents the bucketlist model."""
    title = models.CharField(max_length=255, blank=False, unique=False)
    Genere = models.CharField(max_length=255, blank=False, unique=False)
    image = models.ImageField(upload_to='./image/%Y/%m/%d/', null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='./mp3/320/', null=True, validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
    lyrics = models.FileField(upload_to='./lyrics/%Y/%m/%d/', null=True, validators=[FileExtensionValidator(allowed_extensions=['lrc'])])
    upload_128 = models.FileField(upload_to='./mp3/128/', null=True)
    upload_192 = models.FileField(upload_to='./mp3/192/', null=True)

    

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "Title:{} Genere:{} Image:{} Upload:{} Lyrics:{} upload_128:{} upload_192:{}".format(self.title, self.Genere, self.image, self.upload, self.lyrics, self.upload_128, self.upload_192)