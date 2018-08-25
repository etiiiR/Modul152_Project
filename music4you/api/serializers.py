from rest_framework import serializers
from .models import Music

class MusicSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Music
        fields = ('id', 'title', 'Genere', 'image', 'upload', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')