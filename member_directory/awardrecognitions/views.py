from django.shortcuts import render
from django.http import JsonResponse
from .models import Award

def award_list(request):
    awards = Award.objects.all().values()
    return JsonResponse(list(awards), safe=False)
