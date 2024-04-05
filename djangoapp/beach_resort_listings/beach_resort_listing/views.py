from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Resorts

# Create your views here.

def home(request):

    serialized_resorts = [serialize_resort(resort) for resort in Resorts.objects.all()]

    return render(request, 'home.html', {'resorts': Resorts.objects.all(), 'serialized_resorts': serialized_resorts})

def serialize_resort(resort):
    return {
        "name": resort.name,
        "location": resort.location,
        "desc": resort.desc,
        "price": resort.price,
        "rating": resort.rating,
        "image": resort.image,
        "amenities": resort.amenities,
        "amenityIcons": resort.amenities.split(","),
    }

