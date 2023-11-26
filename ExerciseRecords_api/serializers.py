from rest_framework import serializers
from api.models import ExerciseRecords

class ExerciseRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseRecords
        fields = '__all__'