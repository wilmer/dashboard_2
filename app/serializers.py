from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.Serializer):
    country_name = serializers.CharField()
    country_code = serializers.CharField()
    iso_codes = serializers.CharField()
    population = serializers.IntegerField()
    area = serializers.CharField()
    gdp = serializers.CharField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Country
        field = ('id', 'country_name', 'country_code', 'iso_codes', 'population', 'area', 'gdp',)
        fields = '__all__'
