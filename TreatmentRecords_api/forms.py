from django import forms
from api.models import TreatmentRecords

class TreatmentRecordsforms(forms.ModelForm):
    class Meta:
        model = TreatmentRecords  # 사용할 모델
        fields = '__all__'