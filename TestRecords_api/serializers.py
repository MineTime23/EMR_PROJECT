from rest_framework import serializers
from api.models import TestRecords

class TestRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRecords
        fields = '__all__'