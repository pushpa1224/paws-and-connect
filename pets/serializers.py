from rest_framework import serializers
from .models import Pet, Favorite


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ('created_at',)


class FavoriteSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    pet_id = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all(), source='pet', write_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'pet', 'pet_id', 'created_at')
        read_only_fields = ('created_at',)
