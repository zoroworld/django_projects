from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/pages/index.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from .forms import DocumentForm

def create_doc(request):
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DocumentForm()
    return render(request, "app/pages/create.html", {"form": form})

def home(request):
    docs = Document.objects.order_by("-created_at")
    return render(request, "app/pages/home.html", {"docs": docs})

