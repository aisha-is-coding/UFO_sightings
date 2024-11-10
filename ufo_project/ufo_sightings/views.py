from django.shortcuts import render
from .models import Sighting

# Create your views here.
def map_view(request):
    sightings = Sighting.objects.all()
    context = {
        'sightings': sightings,
    }
    return render(request, 'ufo_sightings/map.html', context)


