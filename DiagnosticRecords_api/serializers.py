from rest_framework import serializers
from api.models import DiagnosticRecords

class DiagnosticRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticRecords
        fields = '__all__'