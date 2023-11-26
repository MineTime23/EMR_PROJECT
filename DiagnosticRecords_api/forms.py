from django import forms
from api.models import DiagnosticRecords

class DiagnosticRecordsforms(forms.ModelForm):
    class Meta:
        model = DiagnosticRecords  # 사용할 모델
        fields = '__all__'
        #fields = ["diagnosis_code", "patient", "user", "diagnosis_date", "symptoms", "diagnosis", " comments"]