from rest_framework import serializers
from .models import Member, AcademicBackground, FamilyDetail, PublicMissionPost, WorkExperience, TrainingCourse, Qualification, AwardsRecognition, DisciplinaryAction, SpecialNote

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['member_id', 'full_name', 'region', 'nation', 'nationality', 'birthday', 'gender', 'department', 'organization', 'current_post', 
                  'position', 'blessing', 'date_of_joining', 'email', 'phone_no', 'address', 'is_deleted']
        read_only_fields = ['member_id']

    def create(self, validated_data):
        validated_data.pop('member_id', None)  # member_id is not set during creation
        return super().create(validated_data)
    
class AcademicBackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicBackground
        fields = ['academic_record_id', 'period', 'school', 'degree', 'graduation']
        read_only_fields = ['academic_record_id']

    def create(self, validated_data):
        validated_data.pop('academic_record_id', None)  # academic_record_id is not set during creation
        return super().create(validated_data)
    
class FamilyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyDetail
        fields = ['family_member_id', 'relation', 'name', 'birthday', 'blessing']
        read_only_fields = ['family_member_id']

    def create(self, validated_data):
        validated_data.pop('family_member_id', None)  # family_member_id is not set during creation
        return super().create(validated_data)
    
class PublicMissionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicMissionPost
        fields = ['mission_id', 'period', 'organization', 'final_position', 'department', 'description']
        read_only_fields = ['mission_id']

    def create(self, validated_data):
        validated_data.pop('mission_id', None)
        return super().create(validated_data)
    
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['experience_id', 'period', 'organization_name', 'final_position', 'department', 'job_description']
        read_only_fields = ['experience_id']

    def create(self, validated_data):
        validated_data.pop('experience_id', None)  # work_experience_id is not set during creation
        return super().create(validated_data)

class TrainingCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCourse
        fields = ['training_id', 'type', 'name_of_course', 'period', 'organization', 'status']
        read_only_fields = ['training_id']

    def create(self, validated_data):
        validated_data.pop('training_id', None)
        return super().create(validated_data)
    
class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ['qualification_id', 'date_acquisition', 'name_qualification', 'remarks']
        read_only_fields = ['qualification_id']

    def create(self, validated_data):
        validated_data.pop('qualification_id', None)  # qualification_id is not set during creation
        return super().create(validated_data)
    
class AwardsRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardsRecognition
        fields = ['award_id', 'date', 'type', 'description', 'organization']
        read_only_fields = ['award_id']

    def create(self, validated_data):
        validated_data.pop('award_id', None)  # award_id is not set during creation
        return super().create(validated_data)
    
class DisciplinaryActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaryAction
        fields = ['penalty_id', 'date', 'reason']
        read_only_fields = ['penalty_id']

    def create(self, validated_data):
        validated_data.pop('penalty_id', None)  # action_id is not set during creation
        return super().create(validated_data)   
    
class SpecialNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialNote
        fields = ['note_id', 'date_written', 'details']
        read_only_fields = ['note_id']

    def create(self, validated_data):
        validated_data.pop('note_id', None)  # note_id is not set during creation
        return super().create(validated_data)



