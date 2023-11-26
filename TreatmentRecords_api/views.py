
from rest_framework.response import Response
from rest_framework import status
from api.models import TreatmentRecords
from TreatmentRecords_api.serializers import TreatmentRecordsSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import TreatmentRecordsforms
from django.http import HttpResponse

def create_Treatment(request):
    if request.method == 'POST':
        form = TreatmentRecordsforms(request.POST)
        if form.is_valid():
            Treatment = form.save(commit=False)
            Treatment.save()
            return HttpResponse("저장이 완료되었습니다. 페이지를 종료하세요.")

    else:
        form = TreatmentRecordsforms()
    context = {'form': form}
    return render(request, 'Treatment_form.html', context)