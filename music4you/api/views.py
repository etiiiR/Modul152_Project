from rest_framework import generics
from .serializers import MusicSerializer
from .models import Music
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