from rest_framework.routers import DefaultRouter
from .api_views import AdoptionRequestViewSet

router = DefaultRouter()
router.register(r'adoptions', AdoptionRequestViewSet, basename='adoption')

urlpatterns = router.urls
