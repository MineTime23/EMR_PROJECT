from django import forms
from api.models import ExerciseRecords

class ExerciseRecordsforms(forms.ModelForm):
    class Meta:
        model = ExerciseRecords  # 사용할 모델
        fields = '__all__'