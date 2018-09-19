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
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        #print(serializer.validated_data['upload'])
        serializer.save()
        



    

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

