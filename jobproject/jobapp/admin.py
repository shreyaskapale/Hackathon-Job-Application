from django.contrib import admin
from .models import UserProfile, ManagerProfile, JobApplication
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ManagerProfile)
admin.site.register(JobApplication)
