from django.urls import path
from . import views

urlpatterns = [
    path('api/academic-records/', views.academic_records_list, name='academic_records_list'),
]
