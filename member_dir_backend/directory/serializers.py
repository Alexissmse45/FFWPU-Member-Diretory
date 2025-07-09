from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ['member_id']

    def create(self, validated_data):
        validated_data.pop('member_id', None)  # member_id is not set during creation
        return super().create(validated_data)

