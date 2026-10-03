from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pets.urls')),
    path('adoptions/', include('adoptions.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('pets.api_urls')),
    path('api/', include('adoptions.api_urls')),
    path('api/auth/', include('accounts.api_urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
