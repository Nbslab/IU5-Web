from rest_framework import viewsets
from city.models import PCs
from city.serializers import PCSerializer


class PCViewSet(viewsets.ModelViewSet):
    queryset = PCs.objects.all().order_by("name")
    serializer_class = PCSerializer
