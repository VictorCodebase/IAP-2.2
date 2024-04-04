from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import imageSuite
# Create your views here.

def home(request):
    resorts = [
        {
            'id': 1,
            'name': "Sunset Paradise Resort",
            'location': "Maldives",
            'desc': "Sunset Paradise Resort is a luxurious beach resort located in the beautiful Maldives. It offers stunning ocean views, spacious rooms, and a wide range of amenities including a swimming pool, spa, and beachfront restaurant.",
            'price': 719000,
            'rating': 4,
            'image': "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            'amenity': ["Swimming Pool", "Spa", "Beachfront Restaurant"],
            'amenityIcon': ["fa-swimming-pool", "fa-spa", "fa-utensils"]
        },
        {
            'id': 2,
            'name': "Tropical Oasis Resort",
            'location': "Bali",
            'desc': "Tropical Oasis Resort is a beachfront resort situated in the stunning Bali. It offers comfortable accommodations, a private beach, and a variety of recreational activities such as water sports and beach volleyball.",
            'price': 233000,
            'rating': 5,
            'image': "https://images.unsplash.com/photo-1535827841776-24afc1e255ac?q=80&w=1635&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            'amenity': ["Private Beach", "Water Sports", "Beach Volleyball"],
            'amenityIcon': ["fa-beach", "fa-swimming", "fa-volleyball-ball"]
        },
        {
            'id': 3,
            'name': "Seaside Retreat Resort",
            'location': "Thailand",
            'desc': "Seaside Retreat Resort is a charming beach resort located in the picturesque Thailand. It offers cozy bungalows, a beachfront bar, and a relaxing atmosphere perfect for a tropical getaway.",
            'price': 89000,
            'rating': 3,
            'image': "https://images.unsplash.com/photo-1619631428089-813ef0fca73b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODB8fHJlc29ydHxlbnwwfHwwfHx8MA%3D%3D",
            'amenity': ["Beachfront Bar", "Cozy Bungalows", "Relaxing Atmosphere"],
            'amenityIcon': ["fa-glass-martini", "fa-campground", "fa-sun"]
        },
        {
            'id': 4,
            'name': "Paradise Cove Resort",
            'location': "Fiji",
            'desc': "Paradise Cove Resort is a secluded beach resort nestled in the pristine Fiji. It offers luxurious villas, a private beach, and a range of activities such as snorkeling, kayaking, and island hopping.",
            'price': 189000,
            'rating': 5,
            'image': "https://images.unsplash.com/photo-1548983615-9e5c3349b637?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDh8fHJlc29ydHxlbnwwfHwwfHx8MA%3D%3D",
            'amenity': ["Luxurious Villas", "Private Beach", "Snorkeling"],
            'amenityIcon': ["fa-hotel", "fa-beach", "fa-swimmer"]
        },
        {
            'id': 5,
            'name': "Coral Sands Resort",
            'location': "Australia",
            'desc': "Coral Sands Resort is a beachfront resort located in the stunning Australia. It offers spacious suites, a beachfront restaurant, and a range of activities such as surfing, fishing, and whale watching.",
            'price': 149000,
            'rating': 4,
            'image': "https://images.unsplash.com/photo-1596178060810-72f53ce9a65c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDR8fHJlc29ydHxlbnwwfHwwfHx8MA%3D%3D",
            'amenity': ["Spacious Suites", "Beachfront Restaurant", "Surfing"],
            'amenityIcon': ["fa-bed", "fa-utensils", "fa-wind"]
        }
    ]

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
    serialized_resorts = json.dumps(resorts)

    return render(request, 'home.html', {'resorts': resorts, 'serialized_resorts': serialized_resorts})

