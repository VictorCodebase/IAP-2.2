from typing import List
from django.db import models

# Create your models here.
class resort:
    id: int
    name: str
    location: str
    desc: str # the description
    price: float
    rating: int
    image: int
    amenity: List[str]
    amenityIcon: List[str]

    def __init__(
        self,
        id: int,
        name: str,
        location: str,
        desc: str,
        price: float,
        rating: int,
        image: int,
        amenity: List[str],
        amenityIcon: List[str]
    ):
        self.id = id
        self.name = name
        self.location = location
        self.desc = desc
        self.price = price
        self.rating = rating
        self.image = image
        self.amenity = amenity
        self.amenityIcon = amenityIcon
# admin.site.register(resort)
