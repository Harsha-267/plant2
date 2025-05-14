from django import forms
from .models import UserPreference

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        fields = ['sunlight', 'water', 'experience', 'location', 'pet_friendly']
        labels = {
            'sunlight': 'Sunlight Availability',
            'water': 'Watering Frequency',
            'experience': 'Your Experience Level',
            'location': 'Plant Location',
            'pet_friendly': 'Pet Friendly Needed'
        }
        widgets = {
            'sunlight': forms.RadioSelect(choices=UserPreference.SUNLIGHT_CHOICES),
            'water': forms.RadioSelect(choices=UserPreference.WATER_CHOICES),
            'experience': forms.RadioSelect(),
            'location': forms.RadioSelect()
        }