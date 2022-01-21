from django.shortcuts import render
from .models import City, Region


def index(request):
    cities = City.objects.all()
    return render(request, 'index.html', {'cities': cities})


def details(request, id):
    city = City.objects.get(id=id)
    return render(request, 'details.html', {'city': city})
