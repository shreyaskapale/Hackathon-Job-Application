from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django.urls import reverse
# Create your models here.

# Job Seeker Model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_regex = RegexValidator(regex=r'^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[6789]\d{9}|(\d[ -]?){10}\d$', message="Please Enter A Valid Mobile Number!")
    phone = models.CharField(validators=[phone_regex], max_length=10)
    profile_pic = models.ImageField(blank = True, upload_to = "profile_pics")

    def __str__(self):
        return self.user.username

# System Manager Model
class ManagerProfile(models.Model):
    manager = models.OneToOneField(User, on_delete = models.CASCADE)
    mgr_id = models.CharField(max_length = 6, unique = True, primary_key = True)
    specification = models.CharField(max_length = 20)

    def __str__(self):
        return self.manager.username

# Job Application Model
class JobApplication(models.Model):
    ROLE_CHOICES = (('SE','Software Engineer'), ('AE', 'Automobile Engineer'), ('DS', 'Data Scientist'), ('BD', 'Backend Developer'), ('FD', 'Frontend Developer'), ('FSD', 'Full Stack Developer'), ('SE', 'System Engineer'), ('DE', 'DevOps Enginner'))
    TYPE_CHOICES = (('FT', 'Full Time'), ('I','Intership'), ('WFH', 'Work From Home'))
    username = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'jobapply', on_delete = models.CASCADE)
    job_role = models.CharField(max_length=40, choices=ROLE_CHOICES)
    work_experience = models.PositiveIntegerField(blank = False)
    skills = models.TextField(max_length=200, blank = False)
    job_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    resume = models.FileField(upload_to="resume")

    def __str__(self):
        return self.username.username

    def get_absolute_url(self):
        return reverse("jobapp:thankyou", kwargs={'pk': self.pk})
