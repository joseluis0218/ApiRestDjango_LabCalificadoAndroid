from django.shortcuts import render
from .models import Solicitud
from .serializers import SolicituSerializer
from rest_framework import viewsets

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all().order_by('id_solicitud')
    serializer_class = SolicituSerializer
