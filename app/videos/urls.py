from django.urls import path
from .views import generate_video, videos_home

urlpatterns = [
    path('', videos_home, name='videos_home'),
    path('generate/', generate_video, name='generate_video'),
]
