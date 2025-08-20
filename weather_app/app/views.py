from django.conf import settings
from django.shortcuts import render
from .utils import get_weather
import os, json

def india_weather_view(request):
    file_path = os.path.join(settings.BASE_DIR, 'app/static/india_weather.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return render(request, 'app/index.html', {"weather": data})

