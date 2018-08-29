from django.db import models
from pydub import AudioSegment
from os import path


# Create your models here.
class Music(models.Model):
    """This class represents the bucketlist model."""
    title = models.CharField(max_length=255, blank=False, unique=False)
    Genere = models.CharField(max_length=255, blank=False, unique=False)
    image = models.ImageField(upload_to='./image/%Y/%m/%d/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    upload = models.FileField(upload_to='./mp3/%Y/%m/%d/test.mp3')
    lyrics = models.FileField(upload_to='./lyrics/%Y/%m/%d/')
    # files                                                                         
    src = "DJ_Khaled_-_Im_The_One_ft._Justin_Bieber_Quavo_Chance_the_Rapper_Lil_Wayn_DoGcdAl.mp3"
    dst = "test.wav"

    print("hello world")

    

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "Title:{} Genere:{} Image:{} Upload:{} Lyrics:{}".format(self.title, self.Genere, self.image, self.upload, self.lyrics)