from django.urls import path
from .views import *

app_name = 'di'

urlpatterns = [
    #path('Diagonostic/',PatientListAPIView.as_view(),name='patient_list'),
    #path('patients/<int:pk>/', PatientDetailAPIView.as_view(), name='patient-detail'),
    path('create_diagnosis/', create_Diagnosis,name='create_Diagnosis'),
]