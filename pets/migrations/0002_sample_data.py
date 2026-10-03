from django.db import migrations


def add_sample_pets(apps, schema_editor):
    Pet = apps.get_model('pets', 'Pet')

    sample_pets = [
        {
            'name': 'Max',
            'animal_type': 'Dog',
            'breed': 'Golden Retriever',
            'age': 2,
            'gender': 'Male',
            'location': 'Dhaka',
            'description': 'Friendly, energetic golden retriever who loves playing fetch and cuddles.',
            'status': 'Available',
        },
        {
            'name': 'Bella',
            'animal_type': 'Cat',
            'breed': 'Persian',
            'age': 1,
            'gender': 'Female',
            'location': 'Chittagong',
            'description': 'Calm, gentle, and affectionate cat looking for a warm home.',
            'status': 'Available',
        },
        {
            'name': 'Rocky',
            'animal_type': 'Dog',
            'breed': 'German Shepherd',
            'age': 3,
            'gender': 'Male',
            'location': 'Dhaka',
            'description': 'Smart, loyal, and very protective companion.',
            'status': 'Available',
        },
        {
            'name': 'Luna',
            'animal_type': 'Cat',
            'breed': 'British Shorthair',
            'age': 2,
            'gender': 'Female',
            'location': 'Sylhet',
            'description': 'Sweet and playful companion with gorgeous green eyes.',
            'status': 'Available',
        },
        {
            'name': 'Snowball',
            'animal_type': 'Rabbit',
            'breed': 'Holland Lop',
            'age': 1,
            'gender': 'Female',
            'location': 'Dhaka',
            'description': 'Cute bunny with floppy ears who loves fresh greens and gentle petting.',
            'status': 'Available',
        },
        {
            'name': 'Charlie',
            'animal_type': 'Bird',
            'breed': 'Cockatiel',
            'age': 2,
            'gender': 'Male',
            'location': 'Rajshahi',
            'description': 'Whistles cheerful tunes and loves perching on shoulders.',
            'status': 'Available',
        },
        {
            'name': 'Daisy',
            'animal_type': 'Dog',
            'breed': 'Beagle',
            'age': 4,
            'gender': 'Female',
            'location': 'Chittagong',
            'description': 'Curious, happy-go-lucky dog who loves outdoor walks.',
            'status': 'Adopted',
        },
    ]

    for data in sample_pets:
        Pet.objects.get_or_create(
            name=data['name'],
            breed=data['breed'],
            defaults=data
        )


def remove_sample_pets(apps, schema_editor):
    Pet = apps.get_model('pets', 'Pet')
    names = ['Max', 'Bella', 'Rocky', 'Luna', 'Snowball', 'Charlie', 'Daisy']
    Pet.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_pets, reverse_code=remove_sample_pets),
    ]
