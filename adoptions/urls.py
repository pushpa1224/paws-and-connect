from django.urls import path
from . import views

urlpatterns = [
    path('pets/<int:pk>/adopt/', views.adoption_form, name='adoption_form'),
    path('my-requests/', views.my_requests, name='my_requests'),
]
