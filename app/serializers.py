from rest_framework import serializers
from .models import ControlOperacional


class ControlOperacionalSerializer(serializers.Serializer):
    nombre_operador = serializers.CharField()
    codigo_equipo = serializers.CharField()
    fecha = serializers.CharField()
    metros_perforados = serializers.IntegerField()
    horas_operacion = serializers.CharField()
    turno = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = ControlOperacional
        field = ('id', 'nombre_operador', 'codigo_equipo', 'fecha', 'metros_perforados', 'horas_operacion', 'turno',)
        fields = '__all__'
