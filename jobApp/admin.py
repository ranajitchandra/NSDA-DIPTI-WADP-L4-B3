from django.contrib import admin

from jobApp.models import *
# Register your models here.

class Custom_user_display(admin.ModelAdmin):
    list_display=['username', 'display_name']
admin.site.register(Custom_User, Custom_user_display)

class job_list(admin.ModelAdmin):
    list_display=['job_title', 'id', 'company_name', 'company_des', 'address', 'qualification', 'salary', 'date_line', 'designation', 'experience', 'created_by']

    search_fields = ['job_title', 'company_name']
    
    fieldsets = [
        (
            'Basic Info', { 'fields': [('job_title', 'company_name', 'company_des', 'address', 'qualification', 'salary', 'date_line', 'designation')] }    
        ),
        (
            'advance', {"classes": ["collapse"], "fields": ["experience", "created_by"],}
        )
    ]
admin.site.register(add_job, job_list)
admin.site.register(jobseeker_profile)
admin.site.register(jobrecruiter_profile)
admin.site.register(educationModel)
admin.site.register(apply_job_model)