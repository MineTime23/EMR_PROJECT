from rest_framework.response import Response
from rest_framework import status
from api.models import DiagnosticRecords
from DiagnosticRecords_api.serializers import DiagnosticRecordsSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import DiagnosticRecordsforms
from django.http import HttpResponse

def create_Diagnosis(request):
    if request.method == 'POST':
        form = DiagnosticRecordsforms(request.POST)
        if form.is_valid():
            DiagnosticRe = form.save(commit=False)
            DiagnosticRe.save()
            return HttpResponse("저장이 완료되었습니다. 페이지를 종료하세요.")

    else:
        form = DiagnosticRecordsforms()
    context = {'form': form}
    return render(request, 'Diagnostic_form.html', context)