from django.shortcuts import render

from videos.models import Video


def videos_home(request):
    if request.user.is_authenticated:
        videos = Video.objects.filter(user_id=request.user)
    else:
        videos = []

    return render(request, 'videos/videos_home.html', {'videos': videos})

