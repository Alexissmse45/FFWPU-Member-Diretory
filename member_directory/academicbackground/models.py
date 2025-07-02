from django.db import models

class AcademicBackground(models.Model):
    academic_record_id = models.AutoField(primary_key=True)
    personnel_id = models.IntegerField()
    period = models.CharField(max_length=100)
    school_university = models.CharField(max_length=255)
    major_degree = models.CharField(max_length=255)
    graduation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.school_university} ({self.period})"
