# myprojects/views.py
from django.http import HttpResponse
import socket

def test_loadbalancer(request):
    hostname = socket.gethostname()  # Each container has a unique hostname
    return HttpResponse(f"Served by container: {hostname}")