# plants/models.py
from django.db import models
from django.conf import settings
import os

def plant_image_path(instance, filename):
    return f'plant_images/{instance.id}/{filename}'

class Plant(models.Model):
    SUNLIGHT_CHOICES = [
        ('low', 'Low Light'),
        ('medium', 'Medium Light'), 
        ('high', 'Bright Light')
    ]
    WATER_CHOICES = [
        ('low', 'Every 2-3 Weeks'),
        ('medium', 'Weekly'),
        ('high', '2-3 Times Weekly')
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('difficult', 'Difficult')
    ]
    LOCATION_CHOICES = [
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
        ('both', 'Indoor/Outdoor')
    ]

    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    sunlight_needs = models.CharField(max_length=20, choices=SUNLIGHT_CHOICES)
    water_needs = models.CharField(max_length=20, choices=WATER_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    pet_friendly = models.BooleanField(default=False)
    image = models.ImageField(upload_to='C:/Users/HP X-360 1030 G2/plant_suggester2/static/images/default-plant.jpeg', blank=True, null=True)


    def __str__(self):
        return f"{self.name} ({self.scientific_name})"
    
    @property
    def image_url(self):
        # Always return the same default image path
        return '/static/images/default-plant.jpg'

class UserPreference(models.Model):
    SUNLIGHT_CHOICES = Plant.SUNLIGHT_CHOICES
    WATER_CHOICES = Plant.WATER_CHOICES
    EXPERIENCE_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert')
    ]
    
    sunlight = models.CharField(max_length=20, choices=SUNLIGHT_CHOICES, verbose_name="Sunlight Available")
    water = models.CharField(max_length=20, choices=WATER_CHOICES, verbose_name="Watering Capacity")
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, verbose_name="Experience Level")
    location = models.CharField(max_length=20, choices=Plant.LOCATION_CHOICES)
    pet_friendly = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Preferences #{self.id}"
