from django.db import models

class AcademicRecord(models.Model):
    academic_record_id = models.AutoField(primary_key=True)
    period = models.CharField(max_length=255)
    school_university = models.CharField(max_length=255)
    major_degree = models.CharField(max_length=255)
    graduation = models.CharField(max_length=255)
    personnel_id = models.IntegerField()

    def __str__(self):
        return f"{self.school_university} - {self.period}"
