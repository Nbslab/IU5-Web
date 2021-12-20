from .models import PCs, Programs
from rest_framework import serializers


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCs
        fields = "__all__"


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = "__all__"