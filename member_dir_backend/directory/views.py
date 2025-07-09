from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializers import MemberSerializer



@api_view(['GET'])
def getDashboard(request):
    return Response('Hello, this is the dashboard!')

@api_view(['GET'])
def getMembers(request):
    members = Member.objects.all()
    serializer = MemberSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['POST'])  
def createMember(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def getMember(request, member_id):
    member = get_object_or_404(Member, member_id=member_id, is_deleted=False)
    serializer = MemberSerializer(member)
    return Response(serializer.data)

@api_view(['PUT'])
def updateMember(request, member_id):
    member = get_object_or_404(Member, member_id=member_id, is_deleted=False)
    serializer = MemberSerializer(member, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteMember(request, member_id):
    member = get_object_or_404(Member, member_id=member_id, is_deleted=False)
    # Soft delete
    member.is_deleted = True
    member.save()
    return Response({'message': 'Member deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
