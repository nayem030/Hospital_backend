from rest_framework import serializers
from . import models

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Services
        fields= '__all__'