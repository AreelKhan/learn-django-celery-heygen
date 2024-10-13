from django.urls import path
from .views import generate_video

urlpatterns = [
    path('generate/', generate_video, name='generate_video'),
]

