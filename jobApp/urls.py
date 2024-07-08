from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobApp.views import *


urlpatterns = [
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('logoutpage/', logoutpage, name='logoutpage'),
    
    path('add_jobPage/', add_jobPage, name='add_jobPage'),
    path('view_job/', view_job, name='view_job'),
    path('editJob/<int:jobPostid>', editJob, name='editJob'),
    path('updatejob/', updatejob, name='updatejob'),
    path('singleview/<int:myid>', singleview, name='singleview'),
    
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('applied_job_by_seeker/', applied_job_by_seeker, name='applied_job_by_seeker'),
    path('posted_by_recruiter/', posted_job_by_recruiter, name='posted_by_recruiter'),
    path('see_applicant/<int:myid>', see_applicant, name='see_applicant'),
    
    path('reject_application/<str:myid>', reject_application, name='reject_application'),
    path('interviewCall/<str:myid>', interviewCall, name='interviewCall'),
    
    path('delete_data/<int:job_id>', delete_data, name='delete_data'),
    path('basic_info/', basic_info, name='basic_info'),
    path('education/', education, name='education'),
    path('update_profile/', update_profile, name='update_profile'),
    path('change_pass/', change_pass, name='change_pass'),
    path('update_pass/', update_pass, name='update_pass'),
    path('view_job_apply/', view_job_apply, name='view_job_apply'),
    path('seach_page/', seach_page, name='seach_page'),
    path('seeker_job_apply/<int:job_id>', seeker_job_apply, name='seeker_job_apply'),
    
    
    path('searchSkill/', searchSkill, name='searchSkill'),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
