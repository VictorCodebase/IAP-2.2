from typing import List
from django.db import models

# Create your models here.
class imageSuite:
    alt: str
    src: str
    desc: str
    def __init__(self, alt: str, src: str, desc: str):
        self.alt = alt
        self.src = src
        self.desc = desc

# admin.site.register(resort)
