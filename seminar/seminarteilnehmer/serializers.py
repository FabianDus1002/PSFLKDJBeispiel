from rest_framework import serializers
from seminarteilnehmer.models import Teilnehmer

class TeilnehmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teilnehmer
        fields = '__all__'