from django.urls import path
from .views import *

app_name = 'tr'

urlpatterns = [
    #path('Diagonostic/',PatientListAPIView.as_view(),name='patient_list'),
    #path('patients/<int:pk>/', PatientDetailAPIView.as_view(), name='patient-detail'),
    path('create_treatment/', create_Treatment,name='create_TreatmentRecords'),
]