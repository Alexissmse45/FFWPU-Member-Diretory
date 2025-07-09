from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDashboard, name='get-dashboard'),
    path('members/', views.getMembers, name='get-members'),
    path('members/create/', views.createMember, name='create-member'),
    path('members/<str:member_id>/', views.getMember, name='get-member'),
    path('members/<str:member_id>/update/', views.updateMember, name='update-member'),
    path('members/<str:member_id>/delete/', views.deleteMember, name='delete-member'),
]