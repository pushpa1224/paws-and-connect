from rest_framework import serializers
from .models import AdoptionRequest
from pets.serializers import PetSerializer


class AdoptionRequestSerializer(serializers.ModelSerializer):
    pet_detail = PetSerializer(source='pet', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = AdoptionRequest
        fields = ('id', 'pet', 'pet_detail', 'username', 'phone', 'address',
                  'reason', 'previous_pet_experience', 'message', 'status', 'created_at')
        read_only_fields = ('status', 'created_at', 'username')

    def validate(self, data):
        user = self.context['request'].user
        pet = data.get('pet')

        if pet and pet.status != 'Available':
            raise serializers.ValidationError('This pet is not available for adoption.')

        if pet and AdoptionRequest.objects.filter(user=user, pet=pet, status='Pending').exists():
            raise serializers.ValidationError('You already have a pending request for this pet.')

        return data
