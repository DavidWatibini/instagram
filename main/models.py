from django.db import models
from datetime import datetime

# Create your models here.
#models for location
class Location(models.Model):
    location_det = models.CharField(max_length=50)

#models for inages
class Image(models.Model):
    username = models.ForeignKey(User)
    image_location = models.ForeignKey(Location)
    image_path = models.ImageField(upload_to = 'gallery/')
    image_description = models.TextField()
    date_posted = db.Column(db.DateTime, 0nullable=False, default=datetime.utcnow)
