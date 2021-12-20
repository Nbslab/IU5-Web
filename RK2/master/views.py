from django.shortcuts import render
from rest_framework import viewsets
from master.models import PCs, Programs
from master.serializers import PCSerializer, ProgramSerializer


def index(request):
    return render(request, 'index.html')


class PCViewSet(viewsets.ModelViewSet):
    queryset = PCs.objects.all().order_by("name")
    serializer_class = PCSerializer


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Programs.objects.all().order_by("name")
    serializer_class = ProgramSerializer


def report(request):
    return render(request, 'report.html', {'data': {'programs': Programs.objects.select_related('pcs')}})
