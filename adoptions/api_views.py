from rest_framework import viewsets, permissions
from .models import AdoptionRequest
from .serializers import AdoptionRequestSerializer


class AdoptionRequestViewSet(viewsets.ModelViewSet):
    serializer_class = AdoptionRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

    def get_queryset(self):
        return AdoptionRequest.objects.filter(user=self.request.user).select_related('pet')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
