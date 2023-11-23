from django.urls import path
from .views import *

app_name = 'pa'

urlpatterns = [
    path('patients/',PatientListAPIView.as_view(),name='patient_list'),
    path('patients/<int:pk>/', PatientDetailAPIView.as_view(), name='patient-detail'),
    path('create_patient/', create_patient,name='create_patient'),
]