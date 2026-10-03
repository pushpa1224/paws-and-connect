from rest_framework import viewsets, permissions
from .models import Pet, Favorite
from .serializers import PetSerializer, FavoriteSerializer
from .filters import PetFilter


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_class = PetFilter
    search_fields = ['name', 'breed', 'location']
    ordering_fields = ['created_at', 'name', 'age']


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user).select_related('pet')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
