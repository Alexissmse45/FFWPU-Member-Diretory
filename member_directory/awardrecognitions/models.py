from django.db import models

class Award(models.Model):
    award_id = models.AutoField(primary_key=True)
    date = models.DateField()
    type = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.CharField(max_length=255)
    personnel_id = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.organization} ({self.date})"

