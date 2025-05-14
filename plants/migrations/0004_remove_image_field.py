from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        # Replace 'previous_migration' with the name of your last migration
        # e.g., if your last migration was 0002_plant_data.py:
        ('plants', '0002_plant_data'),  
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='image',
        ),
    ]