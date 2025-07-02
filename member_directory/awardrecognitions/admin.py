from django.contrib import admin
from .models import Award

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('award_id', 'personnel_id', 'type', 'date', 'organization')
    search_fields = ('award_id', 'personnel_id', 'type', 'organization')
