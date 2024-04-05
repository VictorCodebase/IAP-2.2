from typing import List
from django.db import models

# Create your models here.

class Resorts(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=15)
    desc=models.TextField(max_length=500)
    price=models.IntegerField()
    rating=models.IntegerField()
    image=models.URLField(verbose_name="image url")
    amenities=models.TextField()
    amenityIcons=models.TextField()
    
    
# admin.site.register(resort)
