from django.urls import path
from jobapp import views

app_name = "jobapp"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name='about'),
    path("jobapply/", views.CreateJobView.as_view(), name="jobapply"),
    # path("jobapply/<int:pk>/update/", views.UpdateJobView.as_view(), name="jobupdate"),
    path("jobapply/thankyou", views.thankyou, name="thankyou"),
    path("register/jobseeker", views.register, name="register"),
    path("login/jobseeker", views.user_login, name="user_login"),
    path("register/manager", views.manager_register, name="manager_register"),
    path("login/manager", views.manager_login, name="manager_login"),
]
