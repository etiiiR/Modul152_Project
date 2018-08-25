from django.test import TestCase
from .models import Music
# Create your tests here.

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.music_name = "Write world class code"
        self.music = Music(name=self.music_name)

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Music.objects.count()
        self.music.save()
        new_count = Music.objects.count()
        self.assertNotEqual(old_count, new_count)