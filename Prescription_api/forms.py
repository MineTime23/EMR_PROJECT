from django import forms
from api.models import Prescription

class Prescriptionforms(forms.ModelForm):
    class Meta:
        model = Prescription  # 사용할 모델
        fields = '__all__'