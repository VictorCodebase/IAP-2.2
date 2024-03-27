from django.shortcuts import render

# Create your views here.

def home(request):
    resorts = [
        {
            'name': 'Sunset Paradise Resort',
            'location': 'Maldives',
            'description': 'Sunset Paradise Resort is a luxurious beach resort located in the beautiful Maldives. It offers stunning ocean views, spacious rooms, and a wide range of amenities including a swimming pool, spa, and beachfront restaurant.',
            'price': 119_000,
            'rating': 4,
            'image': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'amenities': [
                {'amenity': 'Swimming Pool', 'icon': 'fa-swimming-pool'},
                {'amenity': 'Spa', 'icon': 'fa-spa'},
                {'amenity': 'Beachfront Restaurant', 'icon': 'fa-utensils'}
            ]
        },
        {
            'name': 'Tropical Oasis Resort',
            'location': 'Bali',
            'description': 'Tropical Oasis Resort is a beachfront resort situated in the stunning Bali. It offers comfortable accommodations, a private beach, and a variety of recreational activities such as water sports and beach volleyball.',
            'price': 233_000,
            'rating': 5,
            'image': 'https://images.unsplash.com/photo-1535827841776-24afc1e255ac?q=80&w=1635&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            'amenities': [
                {'amenity': 'Private Beach', 'icon': 'fa-beach'},
                {'amenity': 'Water Sports', 'icon': 'fa-swimming'},
                {'amenity': 'Beach Volleyball', 'icon': 'fa-volleyball-ball'},
            ]
        },
        {
            'name': 'Seaside Retreat Resort',
            'location': 'Thailand',
            'description': 'Seaside Retreat Resort is a charming beach resort located in the picturesque Thailand. It offers cozy bungalows, a beachfront bar, and a relaxing atmosphere perfect for a tropical getaway.',
            'price': 89_000,
            'rating': 3,
            'image': 'https://images.unsplash.com/photo-1619631428089-813ef0fca73b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODB8fHJlc29ydHxlbnwwfHwwfHx8MA%3D%3D',
            'amenities': [
                {'amenity': 'Beachfront Bar', 'icon': 'fa-glass-martini'},
                {'amenity': 'Cozy Bungalows', 'icon': 'fa-campground'},
                {'amenity': 'Relaxing Atmosphere', 'icon': 'fa-sun'},

            ]
        },
        {
            'name': 'Paradise Cove Resort',
            'location': 'Fiji',
            'description': 'Paradise Cove Resort is a secluded beach resort nestled in the pristine Fiji. It offers luxurious villas, a private beach, and a range of activities such as snorkeling, kayaking, and island hopping.',
            'price': 189_000,
            'rating': 5,
            'image': 'https://images.unsplash.com/photo-1548983615-9e5c3349b637?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDh8fHJlc29ydHxlbnwwfHwwfHx8MA%3D%3D',
            'amenities': [
                {'amenity': 'Luxurious Villas', 'icon': 'fa-hotel'},
                {'amenity': 'Private Beach', 'icon': 'fa-beach'},
                {'amenity': 'Snorkeling', 'icon': 'fa-swimmer'},
            ]
        },
        {
            'name': 'Coral Sands Resort',
            'location': 'Australia',
            'description': 'Coral Sands Resort is a beachfront resort located in the stunning Australia. It offers spacious suites, a beachfront restaurant, and a range of activities such as surfing, fishing, and whale watching.',
            'price': 149_000,
            'rating': 4,
            'image': 'https://images.unsplash.com/photo-1596178060810-72f53ce9a65c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDR8fHJlc29ydHxlbnwwfHwwfHx8MA%3D%3D',
            'amenities': [
                {'amenity': 'Spacious Suites', 'icon': 'fa-bed'},
                {'amenity': 'Beachfront Restaurant', 'icon': 'fa-utensils'},
                {'amenity': 'Surfing', 'icon': 'fa-wind'},
            ]
        },
    ]

    return render(request, 'home.html', {'resorts': resorts})
