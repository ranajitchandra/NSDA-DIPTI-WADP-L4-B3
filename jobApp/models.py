from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Custom_User(AbstractUser):
    USER=[
        ('recruiter', 'Recruter'), ('jobseeker', 'JobSeeker')
    ]
    display_name=models.CharField(max_length=100, null=True)
    user_type=models.CharField(choices=USER, max_length=100, null=True)
    dob=models.CharField(max_length=100, null=True)
    blood=models.CharField(max_length=100, null=True)
    gender=models.CharField(max_length=100, null=True)
    image=models.ImageField(upload_to="static/media", null=True)
    
class add_job(models.Model):
    job_title=models.CharField(max_length=100, null=True)
    company_name=models.CharField(max_length=100, null=True)
    company_des=models.CharField(max_length=100, null=True)
    job_des=models.CharField(max_length=100, null=True)
    address=models.CharField(max_length=100, null=True)
    qualification=models.CharField(max_length=100, null=True)
    salary=models.CharField(max_length=100, null=True)
    date_line=models.CharField(max_length=100, null=True)
    designation=models.CharField(max_length=100, null=True)
    experience=models.CharField(max_length=100, null=True)
    skill=models.CharField(max_length=100, null=True)
    nop=models.CharField(max_length=100, null=True)
    category=models.CharField(max_length=100, null=True)
    created_by=models.ForeignKey(Custom_User, on_delete=models.CASCADE, null=True)
    
class jobseeker_profile(models.Model):
    user=models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='jobseeker_profile')
    skill=models.CharField(max_length=100, null=True)
    resume = models.FileField(upload_to='static/media/applycant_resume', null=True)
    work_exp=models.CharField(max_length=100, null=True)
    highest_edu=models.CharField(max_length=100, null=True)
    def __str__(self) ->str:
        return self.user.first_name+ ' ' +self.user.last_name
    
    
class jobrecruiter_profile(models.Model):
    user=models.OneToOneField(Custom_User, on_delete=models.CASCADE, related_name='jobrecruiter_profile')
    company_name=models.CharField(max_length=100, null=True)
    company_address=models.CharField(max_length=100, null=True)
    
class educationModel(models.Model):
    user=models.ForeignKey(Custom_User, on_delete=models.CASCADE, related_name='educationinfomodel')
    degree=models.CharField(max_length=100, null=True)
    institute=models.CharField(max_length=100, null=True)
    gpa=models.CharField(max_length=100, null=True)
    passingyear=models.CharField(max_length=100, null=True)
    
    def __str__(self) ->str:
        return self.user.first_name+ ' ' +self.user.last_name+ ' '+ self.user.user_type
    
    
class apply_job_model(models.Model):
    applicant = models.ForeignKey(Custom_User, on_delete=models.CASCADE, null=True)
    for_job = models.ForeignKey(add_job, on_delete=models.CASCADE, null=True)
    
    skills = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(upload_to='static/media/applycant_pic', null=True)
    resume = models.FileField(upload_to='static/media/applycant_resume', null=True)
    qualification = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=100, default="Pending", null=True)
    
