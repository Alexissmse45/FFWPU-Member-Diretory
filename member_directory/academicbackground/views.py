from django.shortcuts import render
from django.http import JsonResponse
from .models import AcademicRecord

def academic_records_list(request):
    records = AcademicRecord.objects.all().values()
    return JsonResponse(list(records), safe=False)
