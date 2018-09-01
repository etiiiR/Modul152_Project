from rest_framework import generics
from .serializers import MusicSerializer
from .models import Music
from pydub import AudioSegment
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        print(serializer.validated_data['upload'])
        serializer.save()
        print(serializer.data['upload'].strip('http://localhost:8000/'))
        song_to_sample = serializer.data['upload'].strip('http://localhost:8000/')
        path = "./mp3/320kbit/"
        song = AudioSegment.from_mp3(path  + song_to_sample)
        song.export("mashup.mp3", format="mp3", bitrate="192k")
