from rest_framework.response import Response
from rest_framework import status
from api.models import Patient
from patient_info_api.serializers import PatientSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import PatientForm
from django.http import HttpResponse

class PatientListAPIView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

#    def get(self, request):
#        patients = Patient.objects.all()
#        context = {'patient_list': patients}
#       return render(request, 'base/patient_list.html', context)

def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.save()
            return HttpResponse("저장이 완료되었습니다. 페이지를 종료하세요.")

    else:
        form = PatientForm()
    context = {'form': form}
    return render(request, 'patient_form.html', context)

class PatientDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return None

    def get(self, request, pk):
        patient = self.get_object(pk)
        if patient:
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        patient = self.get_object(pk)
        if patient:
            serializer = PatientSerializer(patient, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        patient = self.get_object(pk)
        if patient:
            patient.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)