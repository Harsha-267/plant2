# plants/admin.py
from django.contrib import admin
from .models import Plant, UserPreference
from django.utils.html import format_html

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'display_image', 'sunlight_needs', 
                   'water_needs', 'difficulty')
    list_filter = ('difficulty', 'location', 'pet_friendly')
    search_fields = ('name', 'scientific_name')
    
    def display_image(self, obj):
        return format_html(
            '<img src="{}" width="50" height="50" style="object-fit: cover;"/>',
            obj.image_url
        )
    display_image.short_description = 'Image'

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sunlight', 'water', 'experience', 'location', 'pet_friendly')
    list_filter = ('experience', 'location', 'pet_friendly')