from django.db import models

class Access(models.Model):
    access_id = models.CharField(max_length=100, primary_key=True)
    personnel_id = models.CharField(max_length=100)
    role_type = models.CharField(max_length=100)
    date_assigned = models.DateField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.access_id} - {self.role_type}"
