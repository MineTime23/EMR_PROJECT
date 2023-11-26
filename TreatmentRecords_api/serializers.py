from rest_framework import serializers
from api.models import TreatmentRecords

class TreatmentRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentRecords
        fields = '__all__'