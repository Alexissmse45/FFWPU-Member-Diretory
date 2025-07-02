from django.contrib import admin
from .models import Access

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ('access_id', 'personnel_id', 'role_type', 'date_assigned')
    search_fields = ('access_id', 'personnel_id', 'role_type')