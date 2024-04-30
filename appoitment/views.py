from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

class AppointmentViewset(viewsets.ModelViewSet):
    queryset=models.Appointment.objects.all()
    serializer_class= serializers.AppointmentSerializers