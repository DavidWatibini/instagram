from django.db import models
from datetime import datetime

# Create your models here.
#models for location
class Location(models.Model):
    location_det = models.CharField(max_length=50)

    def __str__(self):
        return self.location_det

#models for inages
class Image(models.Model):
    image_location = models.ForeignKey(Location)
    image_path = models.ImageField(upload_to = 'gallery/')
    image_description = models.TextField()

    def __str__(self):
        return self.image_description
