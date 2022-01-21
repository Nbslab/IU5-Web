from .models import PCs
from rest_framework import serializers


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCs
        fields = "__all__"