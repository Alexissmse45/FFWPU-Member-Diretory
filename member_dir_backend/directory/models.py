from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'

    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]   

    member_id = models.CharField(primary_key=True, max_length=255)
    #profile_photo_url =
    full_name = models.CharField(max_length=100, null=False, blank=False)
    region = models.CharField(max_length=100, null=False, blank=False)
    nation = models.CharField(max_length=100, null=False, blank=False)
    nationality = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    department = models.CharField(max_length=100, null=True, blank=True) 
    organization = models.CharField(max_length=255, null=True, blank=True)
    current_post = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    blessing = models.CharField(max_length=100, null=False, blank=False)
    date_of_joining = models.DateField(null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    phone_no = models.CharField(max_length=20, null=False, blank=False)
    address = models.TextField(null=False, blank=False) 
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = '"member"."member"'
        verbose_name = "Member"
        verbose_name_plural = "Members"
        managed = False

class AcademicBackground(models.Model):
    academic_record_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=False, blank=False, db_column='member_id')
    period = models.CharField(max_length=100, null=False, blank=False)
    school = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=False)
    graduation = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f"{self.degree} from {self.school} ({self.period})"
    
    class Meta:
        db_table = '"member"."academic_background"'
        verbose_name = "Academic Background"
        verbose_name_plural = "Academic Backgrounds"
        managed = False
    
class FamilyDetail(models.Model):
    family_member_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    relation = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=True, blank=True)
    blessing = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = '"member"."family_detail"'
        verbose_name = "Family Detail"
        verbose_name_plural = "Family Details"
        managed = False


class PublicMissionPost(models.Model):
    mission_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    period = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)
    final_position = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = '"member"."public_mission_post"'
        verbose_name = "Public Mission Post"
        verbose_name_plural = "Public Mission Posts"
        managed = False


class WorkExperience(models.Model):
    experience_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    period = models.CharField(max_length=100, null=True, blank=True)
    organization_name = models.CharField(max_length=255, null=True, blank=True)
    final_position = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = '"member"."work_experience"'
        verbose_name = "Work Experience"
        verbose_name_plural = "Work Experiences"
        managed = False


class TrainingCourse(models.Model):
    training_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    type = models.CharField(max_length=100, null=True, blank=True)
    name_of_course = models.CharField(max_length=255, null=True, blank=True)
    period = models.CharField(max_length=100, null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = '"member"."training_course"'
        verbose_name = "Training Course"
        verbose_name_plural = "Training Courses"
        managed = False


class Qualification(models.Model):
    qualification_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    date_acquisition = models.DateField(null=True, blank=True)
    name_qualification = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = '"member"."qualification"'
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"
        managed = False


class AwardsRecognition(models.Model):
    award_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    organization = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = '"member"."awards_recognition"'
        verbose_name = "Award/Recognition"
        verbose_name_plural = "Awards & Recognitions"
        managed = False


class DisciplinaryAction(models.Model):
    penalty_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    date = models.DateField(null=True, blank=True)
    reason = models.TextField(null=False, blank=False)

    class Meta:
        db_table = '"member"."disciplinary_action"'
        verbose_name = "Disciplinary Action"
        verbose_name_plural = "Disciplinary Actions"
        managed = False


class SpecialNote(models.Model):
    note_id = models.CharField(primary_key=True, max_length=255)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, db_column='member_id')
    date_written = models.DateField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    class Meta:
        db_table = '"member"."special_note"'
        verbose_name = "Special Note"
        verbose_name_plural = "Special Notes"
        managed = False


class AdminAccount(models.Model):
    account_id = models.CharField(primary_key=True, max_length=255)
    email = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    img_path = models.CharField(max_length=255, null=True, blank=True)
    permission = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = '"admin"."admin_account"'
        verbose_name = "Admin Account"
        verbose_name_plural = "Admin Accounts"
        managed = False



