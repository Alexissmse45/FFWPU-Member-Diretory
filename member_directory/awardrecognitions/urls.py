from django.urls import path
from . import views

urlpatterns = [
    path('api/awards/', views.award_list, name='award_list'),
]
