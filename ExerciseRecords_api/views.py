from rest_framework.response import Response
from rest_framework import status
from api.models import ExerciseRecords
from ExerciseRecords_api.serializers import ExerciseRecordsSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import ExerciseRecordsforms
from django.http import HttpResponse

def create_ExerciseRecords(request):
    if request.method == 'POST':
        form = ExerciseRecordsforms(request.POST)
        if form.is_valid():
            ExerciseRecords = form.save(commit=False)
            ExerciseRecords.save()
            return HttpResponse("저장이 완료되었습니다. 페이지를 종료하세요.")

    else:
        form = ExerciseRecordsforms()
    context = {'form': form}
    return render(request, 'Exercise_form.html', context)