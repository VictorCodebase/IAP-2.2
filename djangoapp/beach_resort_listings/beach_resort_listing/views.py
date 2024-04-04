from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.

def home(request):
    img1 = imageSuite("resort Image", "https://images.pexels.com/photos/4825719/pexels-photo-4825719.jpeg?auto=compress&cs=tinysrgb&w=600", "interior")
    img2 = imageSuite("resort Image", "https://images.pexels.com/photos/4993046/pexels-photo-4993046.jpeg?auto=compress&cs=tinysrgb&w=600", "interior")
    img3 = imageSuite("resort Image", "https://images.pexels.com/photos/6394559/pexels-photo-6394559.jpeg?auto=compress&cs=tinysrgb&w=600", "interior")
    img4 = imageSuite("resort Image", "https://images.pexels.com/photos/6130081/pexels-photo-6130081.jpeg?auto=compress&cs=tinysrgb&w=600", "interior")
    img5 = imageSuite("resort Image", "https://images.pexels.com/photos/18185785/pexels-photo-18185785/free-photo-of-deckchairs-and-umbrellas-on-beach-in-alghero-italy.jpeg?auto=compress&cs=tinysrgb&w=600", "exterior")
    img6 = imageSuite("resort Image", "https://images.pexels.com/photos/18201284/pexels-photo-18201284/free-photo-of-thatched-houses-on-fishermans-island-in-le-barcares.jpeg?auto=compress&cs=tinysrgb&w=600", "exterior")
    img7 = imageSuite("resort Image", "https://images.pexels.com/photos/3144978/pexels-photo-3144978.jpeg?auto=compress&cs=tinysrgb&w=600", "exterior")
    img8 = imageSuite("resort Image", "https://images.pexels.com/photos/4577191/pexels-photo-4577191.jpeg?auto=compress&cs=tinysrgb&w=600", "exterior")
    img9 = imageSuite("resort Image", "https://images.pexels.com/photos/2631613/pexels-photo-2631613.jpeg?auto=compress&cs=tinysrgb&w=600", "interior")
    img10 = imageSuite("resort Image", "https://images.pexels.com/photos/338504/pexels-photo-338504.jpeg?auto=compress&cs=tinysrgb&w=600", "exterior")
    images = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10]
    
    #had to change this up as we were no longer getting the values to serialize from an array
    serialized_resorts = [serialize_resort(resort) for resort in Resorts.objects.all()]

    return render(request, 'home.html', {'resorts': Resorts.objects.all(), 'serialized_resorts': serialized_resorts})

def serialize_resort(resort):
    return {
        'name': resort.name,
        'location': resort.location,
        'desc': resort.desc,
        'price': resort.price,
        'rating': resort.rating,
        'image': resort.image,
        'amenities': resort.amenities,
        'amenityIcons': resort.amenities.split(","),
    }

