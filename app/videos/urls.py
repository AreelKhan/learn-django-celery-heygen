from django.urls import path
from .views import videos_home

urlpatterns = [
    path('', videos_home, name='videos_home'),
]
