from rest_framework.response import Response
from rest_framework import status
from api.models import Prescription
from Prescription_api.serializers import PrescriptionSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import Prescriptionforms
from django.http import HttpResponse

def create_Prescription(request):
    if request.method == 'POST':
        form = Prescriptionforms(request.POST)
        if form.is_valid():
            Prescription = form.save(commit=False)
            Prescription.save()
            return HttpResponse("저장이 완료되었습니다. 페이지를 종료하세요.")

    else:
        form = Prescriptionforms()
    context = {'form': form}
    return render(request, 'Prescription_form.html', context)