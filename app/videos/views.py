from django.shortcuts import render


def generate_video(request):
    return render(request, 'videos/generate.html')
