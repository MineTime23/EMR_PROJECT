from django.urls import path
from .views import *

urlpatterns = [
    path('TestRecords/<int:pk>/', TestRecordsAPIView.as_view(), name='TestRecords-detail'),
    path('create_TestRecords/', create_TestRecords, name='create_TestRecords'),
]