from rest_framework import generics
from .serializers import MusicSerializer
from .models import Music
from pydub import AudioSegment
import logging
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        print(serializer.validated_data['upload'])
        serializer.save()
        print(serializer.data['upload'].strip('http://localhost:8001/'))
        song_to_sample = serializer.data['upload'].strip('http://localhost:8001/')
        song = AudioSegment.from_mp3(song_to_sample)
        export_song_name = serializer.data['upload'].strip('http://localhost:8001/media/mp3/320/')
        song.export("/app/media/mp3/192/" + export_song_name + "mp3" , format="mp3", bitrate="192k")
        song.export("/app/media/mp3/128/" + export_song_name + "mp3" , format="mp3", bitrate="128k")
