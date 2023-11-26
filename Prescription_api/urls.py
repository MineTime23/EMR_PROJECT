from django.urls import path
from .views import *

app_name = 'pr'

urlpatterns = [
    #path('Diagonostic/',PatientListAPIView.as_view(),name='patient_list'),
    #path('patients/<int:pk>/', PatientDetailAPIView.as_view(), name='patient-detail'),
    path('create_prescription/', create_Prescription,name='create_Diagnosis'),
]