from rest_framework import serializers
from .models import Solicitud

class SolicituSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id_solicitud','correo','tipo','motivo','voucher')