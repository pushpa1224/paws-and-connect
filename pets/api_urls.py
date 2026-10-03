from rest_framework.routers import DefaultRouter
from .api_views import PetViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'pets', PetViewSet, basename='pet')
router.register(r'favorites', FavoriteViewSet, basename='favorite')

urlpatterns = router.urls
