from django.db import models
from pydub import AudioSegment
from os import path
from django.core.validators import FileExtensionValidator
from .validators import validate_file_size


# Create your models here.
class Music(models.Model):
    """This class represents the bucketlist model.
        The title of the Model is as it named self explaining
    """
    title = models.CharField(max_length=255, blank=False, unique=False)
    Genere = models.CharField(max_length=255, blank=False, unique=False)
    image = models.ImageField(upload_to='./image/%Y/%m/%d/', default='/app/media/placeholder.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png']), validate_file_size])
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='./mp3/320/', validators=[FileExtensionValidator(allowed_extensions=['mp3']), validate_file_size])
    lyrics = models.FileField(upload_to='./lyrics/%Y/%m/%d/', default='/app/media/Adele_-_Hello.lrc', validators=[FileExtensionValidator(allowed_extensions=['lrc']), validate_file_size])
    upload_128 = models.FileField(upload_to='./mp3/128/', blank=True, null=True)
    upload_192 = models.FileField(upload_to='./mp3/192/', blank=True, null=True)

    

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "Title:{} Genere:{} Image:{} Upload:{} Lyrics:{} upload_128:{} upload_192:{}".format(self.title, self.Genere, self.image, self.upload, self.lyrics, self.upload_128, self.upload_192)