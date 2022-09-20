from django.shortcuts import render
from .models import Objects

# Create your views here.

def index(request):
    objs = Objects.objects.get()
    return render(request, 'index.html', {'objs':objs})

