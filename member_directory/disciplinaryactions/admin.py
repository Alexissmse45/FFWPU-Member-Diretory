from django.contrib import admin
from .models import Penalty

@admin.register(Penalty)
class PenaltyAdmin(admin.ModelAdmin):
    list_display = ('penalty_id', 'personnel_id', 'date')
    search_fields = ('penalty_id', 'personnel_id', 'reason')
