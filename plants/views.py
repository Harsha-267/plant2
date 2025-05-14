from django.shortcuts import render, redirect
from .models import Plant, UserPreference
from .forms import PreferenceForm
def home(request):
    """Home page view that shows the main landing page"""
    return render(request, 'home.html')

def plant_list(request):
    """View to show all plants"""
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})

def suggest_plants(request):
    """View to handle plant suggestions"""
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            preferences = form.save()
            
             # Get matching plants with image handling
            suggested_plants = Plant.objects.filter(
                sunlight_needs__lte=preferences.sunlight,
                water_needs__lte=preferences.water,
                location__in=[preferences.location, 'both']
            ).order_by('?')[:2]  # Get 2 random matching plants
            
            # Get matching plants based on preferences with priority scoring
            sunlight = preferences.sunlight  # Changed from sunlight
            water = preferences.water       # Changed from water
            experience = preferences.experience
            location = preferences.location
            
            # Create a queryset of potentially suitable plants
            suitable_plants = Plant.objects.filter(
                sunlight_needs__lte=sunlight,
                water_needs__lte=water,
                location__in=[location, 'both']
            ).order_by('?')[:2]
            
            # Score each plant based on how well it matches preferences
            scored_plants = []
            for plant in suitable_plants:
                score = 0
                
                # Score sunlight match (exact match gets higher score)
                if plant.sunlight_needs == sunlight:
                    score += 3
                else:
                    score += 1
                
                # Score water match
                if plant.water_needs == water:
                    score += 3
                else:
                    score += 1
                
                # Score experience level match
                if (experience == 'beginner' ):
                    score += 5
                elif (experience == 'intermediate' ):
                    score += 3
                else:
                    score += 1
                
                scored_plants.append((score, plant))
            
            # Sort by score (highest first) and get top 2
            scored_plants.sort(reverse=True, key=lambda x: x[0])
            top_plants = [plant for (score, plant) in scored_plants[:2]]
            
            return render(request, 'suggestions.html', {
                'plants': top_plants,
                'preferences': preferences
            })
    else:
        form = PreferenceForm()
    return render(request, 'preferences.html', {'form': form})