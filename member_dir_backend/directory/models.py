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
