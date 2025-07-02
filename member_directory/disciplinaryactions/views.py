from django.shortcuts import render
from rest_framework import viewsets
from .models import Penalty
from .serializers import PenaltySerializer

class PenaltyViewSet(viewsets.ModelViewSet):
    queryset = Penalty.objects.all()
    serializer_class = PenaltySerializer
