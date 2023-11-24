from django import forms
from api.models import TestRecords

class TestRecordsForm(forms.ModelForm):
    class Meta:
        model = TestRecords  # 사용할 모델
        fields = ["test_code", "patient", "MuscleMass", "BodyFatMass", "Muscular_strength", "cardio_endurance", "agility", "flexibility", "date"]