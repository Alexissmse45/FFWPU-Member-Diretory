from django.shortcuts import render
from rest_framework import viewsets
from .models import Award
from .serializers import AwardSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

