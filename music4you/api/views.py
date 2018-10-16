from rest_framework import generics
from .serializers import MusicSerializer
from .models import Music
from pydub import AudioSegment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MusicSerializer
from rest_framework import mixins
from .models import *
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os, sys
import requests
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        #print(serializer.validated_data['upload'])
        before_save = serializer.save()
        song_to_sample = serializer.data['upload'].strip('http://localhost:8001/')
        song = AudioSegment.from_mp3(song_to_sample)
        export_song_name = serializer.data['upload'].strip('http://localhost:8001/media/mp3/320/')
        paths = "/app/media/mp3/192/"
        if not os.path.exists(paths):
            os.makedirs(paths)
        song.export("/app/media/mp3/192/" + export_song_name + "mp3" , format="mp3", bitrate="192k")
        paths = "/app/media/mp3/128/"
        if not os.path.exists(paths):
            os.makedirs(paths)
        hello = song.export("/app/media/mp3/128/" + export_song_name + "mp3" , format="mp3", bitrate="128k")
        number_of_id = serializer.data['id']
        p = Music.objects.get(pk=number_of_id)
        p.upload_128 = 'mp3/128/' + export_song_name + "mp3"
        p.upload_192 = 'mp3/192/' + export_song_name + "mp3"
        p.save()
        headers = {"Content-Type" : "application/json"}
        url = 'http://localhost:8001/number_of_id/delete/'
        r = requests.delete(url, headers=headers)

    

class UserUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = MusicSerializer
    model = Music

    def get_queryset(self):
        queryset = self.model.objects.filter()
        return queryset

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UsersListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class UserDeleteView(generics.ListAPIView, mixins.DestroyModelMixin):
    queryset = Music.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
class GEToneResult(generics.RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

