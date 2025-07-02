from django.contrib import admin
from .models import AuditLog

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('log_in', 'user_id', 'action', 'timestamp', 'ip_address')
    search_fields = ('log_in', 'user_id', 'action', 'ip_address')