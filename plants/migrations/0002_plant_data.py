from django.db import migrations

def load_plant_data(apps, schema_editor):
    Plant = apps.get_model('plants', 'Plant')
    
    plant_data = [
        # 1-10
        {
            'name': 'Snake Plant',
            'scientific_name': 'Sansevieria trifasciata',
            'description': 'Hardy low-light plant with tall, stiff leaves',
            'sunlight_needs': 'low',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Peace Lily',
            'scientific_name': 'Spathiphyllum wallisii',
            'description': 'Tropical plant with white flowers, loves humidity',
            'sunlight_needs': 'medium',
            'water_needs': 'high',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Aloe Vera',
            'scientific_name': 'Aloe barbadensis',
            'description': 'Succulent with medicinal gel, needs good drainage',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'both',
            'pet_friendly': True
        },
        {
            'name': 'Spider Plant',
            'scientific_name': 'Chlorophytum comosum',
            'description': 'Produces baby plantlets, great for hanging baskets',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Jade Plant',
            'scientific_name': 'Crassula ovata',
            'description': 'Tree-like succulent with thick oval leaves',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'both',
            'pet_friendly': False
        },
        {
            'name': 'Rubber Plant',
            'scientific_name': 'Ficus elastica',
            'description': 'Large glossy leaves, grows tall indoors',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'ZZ Plant',
            'scientific_name': 'Zamioculcas zamiifolia',
            'description': 'Tolerates low light and irregular watering',
            'sunlight_needs': 'low',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Pothos',
            'scientific_name': 'Epipremnum aureum',
            'description': 'Trailing vine, very easy to grow',
            'sunlight_needs': 'low',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Monstera',
            'scientific_name': 'Monstera deliciosa',
            'description': 'Large split leaves, tropical appearance',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Fiddle Leaf Fig',
            'scientific_name': 'Ficus lyrata',
            'description': 'Large violin-shaped leaves, needs consistent care',
            'sunlight_needs': 'high',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },

        # 11-20
        {
            'name': 'Chinese Money Plant',
            'scientific_name': 'Pilea peperomioides',
            'description': 'Round leaves on upright stems, easy to propagate',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'String of Pearls',
            'scientific_name': 'Senecio rowleyanus',
            'description': 'Trailing succulent with bead-like leaves',
            'sunlight_needs': 'medium',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Bird of Paradise',
            'scientific_name': 'Strelitzia reginae',
            'description': 'Tropical plant with large banana-like leaves',
            'sunlight_needs': 'high',
            'water_needs': 'medium',
            'location': 'both',
            'pet_friendly': False
        },
        {
            'name': 'Calathea',
            'scientific_name': 'Calathea spp.',
            'description': 'Beautiful patterned leaves, needs humidity',
            'sunlight_needs': 'medium',
            'water_needs': 'high',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Philodendron',
            'scientific_name': 'Philodendron spp.',
            'description': 'Heart-shaped leaves, easy to care for',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Basil',
            'scientific_name': 'Ocimum basilicum',
            'description': 'Popular culinary herb, needs regular harvesting',
            'sunlight_needs': 'high',
            'water_needs': 'high',
            'location': 'outdoor',
            'pet_friendly': True
        },
        {
            'name': 'Mint',
            'scientific_name': 'Mentha spp.',
            'description': 'Fast-growing herb, can be invasive',
            'sunlight_needs': 'medium',
            'water_needs': 'high',
            'location': 'outdoor',
            'pet_friendly': True
        },
        {
            'name': 'Lavender',
            'scientific_name': 'Lavandula spp.',
            'description': 'Fragrant purple flowers, loves sun',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'outdoor',
            'pet_friendly': True
        },
        {
            'name': 'Rosemary',
            'scientific_name': 'Rosmarinus officinalis',
            'description': 'Fragrant herb used in cooking',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'outdoor',
            'pet_friendly': True
        },
        {
            'name': 'Tomato',
            'scientific_name': 'Solanum lycopersicum',
            'description': 'Popular fruiting plant that needs support',
            'sunlight_needs': 'high',
            'water_needs': 'high',
            'location': 'outdoor',
            'pet_friendly': True
        },

        # 21-30
        {
            'name': 'English Ivy',
            'scientific_name': 'Hedera helix',
            'description': 'Trailing vine, good for hanging baskets',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Bamboo Palm',
            'scientific_name': 'Chamaedorea seifrizii',
            'description': 'Tropical palm that purifies air',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Dracaena',
            'scientific_name': 'Dracaena spp.',
            'description': 'Architectural plant with striped leaves',
            'sunlight_needs': 'medium',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Areca Palm',
            'scientific_name': 'Dypsis lutescens',
            'description': 'Feathery fronds, great for bright spaces',
            'sunlight_needs': 'high',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Parlor Palm',
            'scientific_name': 'Chamaedorea elegans',
            'description': 'Compact palm for low light conditions',
            'sunlight_needs': 'low',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'String of Hearts',
            'scientific_name': 'Ceropegia woodii',
            'description': 'Trailing plant with heart-shaped leaves',
            'sunlight_needs': 'medium',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Peperomia',
            'scientific_name': 'Peperomia spp.',
            'description': 'Compact plant with varied leaf shapes',
            'sunlight_needs': 'medium',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Hoya',
            'scientific_name': 'Hoya spp.',
            'description': 'Waxy leaves with fragrant flowers',
            'sunlight_needs': 'medium',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Strawberry',
            'scientific_name': 'Fragaria × ananassa',
            'description': 'Fruit-bearing plant that spreads via runners',
            'sunlight_needs': 'high',
            'water_needs': 'high',
            'location': 'outdoor',
            'pet_friendly': True
        },
        {
            'name': 'Lemon Tree',
            'scientific_name': 'Citrus limon',
            'description': 'Dwarf varieties can grow indoors',
            'sunlight_needs': 'high',
            'water_needs': 'medium',
            'location': 'both',
            'pet_friendly': True
        },

        # 31-40
        {
            'name': 'Cactus',
            'scientific_name': 'Cactaceae family',
            'description': 'Diverse group of succulents with minimal water needs',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'both',
            'pet_friendly': False
        },
        {
            'name': 'Succulent',
            'scientific_name': 'Various',
            'description': 'Drought-resistant plants with thick leaves',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'both',
            'pet_friendly': True
        },
        {
            'name': 'Orchid',
            'scientific_name': 'Phalaenopsis spp.',
            'description': 'Elegant flowering plant with long-lasting blooms',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'African Violet',
            'scientific_name': 'Saintpaulia ionantha',
            'description': 'Compact flowering plant for windowsills',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Begonia',
            'scientific_name': 'Begonia spp.',
            'description': 'Colorful foliage and flowers',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Coleus',
            'scientific_name': 'Plectranthus scutellarioides',
            'description': 'Vibrant colorful foliage plant',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'both',
            'pet_friendly': True
        },
        {
            'name': 'Fern',
            'scientific_name': 'Various',
            'description': 'Lush green foliage, loves humidity',
            'sunlight_needs': 'low',
            'water_needs': 'high',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Bromeliad',
            'scientific_name': 'Bromeliaceae family',
            'description': 'Tropical plant with colorful central "flower"',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Air Plant',
            'scientific_name': 'Tillandsia spp.',
            'description': 'Grows without soil, absorbs moisture from air',
            'sunlight_needs': 'medium',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Kalanchoe',
            'scientific_name': 'Kalanchoe blossfeldiana',
            'description': 'Succulent with clusters of small flowers',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'both',
            'pet_friendly': False
        },

        # 41-50
        {
            'name': 'Schefflera',
            'scientific_name': 'Schefflera arboricola',
            'description': 'Umbrella-shaped leaves on woody stems',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Croton',
            'scientific_name': 'Codiaeum variegatum',
            'description': 'Colorful variegated leaves, needs bright light',
            'sunlight_needs': 'high',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Dieffenbachia',
            'scientific_name': 'Dieffenbachia spp.',
            'description': 'Large variegated leaves, toxic if ingested',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Polka Dot Plant',
            'scientific_name': 'Hypoestes phyllostachya',
            'description': 'Colorful spotted foliage, compact growth',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Ponytail Palm',
            'scientific_name': 'Beaucarnea recurvata',
            'description': 'Drought-tolerant with bulbous trunk',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'both',
            'pet_friendly': True
        },
        {
            'name': 'Cast Iron Plant',
            'scientific_name': 'Aspidistra elatior',
            'description': 'Nearly indestructible, tolerates neglect',
            'sunlight_needs': 'low',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': True
        },
        {
            'name': 'Chinese Evergreen',
            'scientific_name': 'Aglaonema spp.',
            'description': 'Colorful patterned leaves, low maintenance',
            'sunlight_needs': 'low',
            'water_needs': 'low',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Ficus',
            'scientific_name': 'Ficus benjamina',
            'description': 'Weeping fig with small pointed leaves',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        },
        {
            'name': 'Yucca',
            'scientific_name': 'Yucca elephantipes',
            'description': 'Architectural plant with sword-like leaves',
            'sunlight_needs': 'high',
            'water_needs': 'low',
            'location': 'both',
            'pet_friendly': False
        },
        {
            'name': 'Swiss Cheese Plant',
            'scientific_name': 'Monstera adansonii',
            'description': 'Climbing plant with holey leaves',
            'sunlight_needs': 'medium',
            'water_needs': 'medium',
            'location': 'indoor',
            'pet_friendly': False
        }
    ]
    
    for plant in plant_data:
        Plant.objects.create(**plant)

class Migration(migrations.Migration):
    dependencies = [
        ('plants', '0001_initial'),
    ]
    operations = [
        migrations.RunPython(load_plant_data),
    ]