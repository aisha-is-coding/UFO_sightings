from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Sighting(models.Model):
    datetime = models.DateTimeField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=2)
    ufo_shape = models.CharField(max_length=50, null=True, blank=True)
    duration_seconds = models.FloatField()
    duration_reported = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    date_documented = models.DateField()
    location = models.PointField(geography=True, srid=4326) # Pointfield store geographic coordinates

    def __str__(self):
        return f"Sighting at {self.city}, {self.country} on {self.datetime}"
    

