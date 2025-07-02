from rest_framework import serializers
from .models import AcademicBackground

class AcademicBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicBackground
        fields = '__all__'