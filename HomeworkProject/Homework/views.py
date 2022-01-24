from django.shortcuts import render
from .models import City, Region
from django.views import generic

from .forms import CityUpdateForm


def index(request):
    cities = City.objects.all()
    return render(request, 'index.html', {'cities': cities})


def details(request, id):
    city = City.objects.get(id=id)
    return render(request, 'details.html', {'city': city})


def report(request):
    cities = City.objects.all()
    return render(request, 'report.html', {'cities': cities})


class CityUpdateView(generic.UpdateView):
    """Изменение города"""
    model = City
    template_name = "update.html"
    form_class = CityUpdateForm
