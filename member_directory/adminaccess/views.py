from django.shortcuts import render
from rest_framework import viewsets
from .models import Access
from .serializers import AccessSerializer

class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer