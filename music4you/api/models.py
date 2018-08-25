from django.db import models

# Create your models here.
class Music(models.Model):
    """This class represents the bucketlist model."""
    title = models.CharField(max_length=255, blank=False, unique=False)
    Genere = models.CharField(max_length=255, blank=False, unique=False)
    image = models.ImageField(upload_to='./image/%Y/%m/%d/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='./mp3/%Y/%m/%d/')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "Title:{} Genere:{} Image:{} Upload:{}".format(self.title, self.Genere, self.image, self.upload)