from django.db import models

class Penalty(models.Model):
    penalty_id = models.CharField(max_length=100, primary_key=True)
    personnel_id = models.CharField(max_length=100)
    date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.penalty_id} - {self.reason[:30]}"
