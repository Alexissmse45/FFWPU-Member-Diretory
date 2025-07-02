from django.db import models

class AuditLog(models.Model):
    log_in = models.CharField(max_length=100, primary_key=True)
    user_id = models.CharField(max_length=100)
    action = models.TextField()
    timestamp = models.DateTimeField()
    ip_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.log_in} - {self.user_id} - {self.action}"