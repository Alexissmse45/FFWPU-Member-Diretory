from django.db import models

class Award(models.Model):
    award_id = models.CharField(max_length=100, primary_key=True)
    personnel_id = models.CharField(max_length=100)
    date = models.DateField()
    type = models.CharField(max_length=100)
    description = models.TextField()
    organization = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.award_id} - {self.type}"