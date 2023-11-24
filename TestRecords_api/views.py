from rest_framework.response import Response
from rest_framework import status
from api.models import TestRecords
from TestRecords_api.serializers import TestRecordsSerializer
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .forms import TestRecordsForm
from django.http import HttpResponse

class TestRecordsAPIView(APIView):
    def get_object(self, pk):
        try:
            return TestRecords.objects.get(pk=pk)
        except TestRecords.DoesNotExist:
            return None

    def get(self, request, pk):
        TestRecord = self.get_object(pk)
        if TestRecord:
            serializer = TestRecordsSerializer(TestRecord)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

def create_TestRecords(request):
    if request.method == 'POST':
        form = TestRecordsForm(request.POST)
        if form.is_valid():
            TestRecords = form.save(commit=False)
            TestRecords.save()
            return HttpResponse("저장이 완료되었습니다. 페이지를 종료하세요.")

    else:
        form = TestRecordsForm()
    context = {'form': form}
    return render(request, 'TestRecord_form.html', context)