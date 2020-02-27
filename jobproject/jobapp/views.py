from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from .models import JobApplication
from .forms import (UserForm, UserProfileForm, ManagerForm, ManagerProfileForm, JobApplicationForm)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request, "index.html", {"friend":"To Job Portal"})

def thankyou(request):
    return render(request, "thankyou.html", {})

class AboutView(TemplateView):
    template_name = 'about.html'

# Job Seeker LogOut
@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

# System Manager LogOut
@login_required
def manager_logout(request):
    # Log out the manager.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

#Job Seeker Registration
def register(request):

    registered = False
    name = "Customer"

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        name = request.POST.get("first_name")
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    cust_dict = {
        "registered" : registered,
        "user_form" : user_form,
        "profile_form" : profile_form,
        "username" : name,
    }
    return render(request, "authentication/registration.html", context = cust_dict)

#System Manager Registration
def manager_register(request):
    registered = False
    name = "Manager"

    if request.method == "POST":
        manager_form = ManagerForm(request.POST)
        profile_form = ManagerProfileForm(request.POST)
        name = request.POST.get("first_name")
        if manager_form.is_valid() and profile_form.is_valid():
            manager = manager_form.save()
            manager.set_password(manager.password)
            manager.is_staff = True
            manager.is_superuser = True
            manager.save()

            profile = profile_form.save(commit=False)
            profile.manager = manager

            profile.save()
            registered = True
        else:
            print(manager_form.errors, profile_form.errors)
    else:
        manager_form = ManagerForm()
        profile_form = ManagerProfileForm()

    manage_dict = {
        "registered" : registered,
        "manager_form" : manager_form,
        "profile_form" : profile_form,
        "username" : name,
    }
    return render(request, "authentication/registration.html", context = manage_dict)

# Job Seeker Login
def user_login(request):
    who = ''
    if request.method == 'POST':
    # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check if the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                who = 'jobseeker'
                # Send the user back to some page.
                # In this case their homepage.
                return render(request, "index.html", {"friend" : username, 'who' : who})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'authentication/invalid_login.html')
    else:
        #Nothing has been provided for username or password.
        return render(request, 'authentication/login.html', {})


# System Manager Login
def manager_login(request):
    who = ''
    if request.method == 'POST':
    # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django's built-in authentication function:
        manager = authenticate(username=username, password=password)

        # If we have a manager
        if manager:
            #Check it the account is active
            if manager.is_active:
                # Log the user in.
                login(request,manager)
                who = 'manager'
                # Send the manager back to some page.
                # In this case their homepage.
                return render(request, "index.html", {"friend" : username, 'who' : who})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request, 'authentication/invalid_login.html')
    else:
        #Nothing has been provided for username or password.
        return render(request, 'authentication/login.html', {})

class CreateJobView(LoginRequiredMixin, CreateView):
    login_url = '/login/jobseeker/'
    redirect_field_name = 'index.html'
    form_class = JobApplicationForm
    model = JobApplication
class UpdateJobView(LoginRequiredMixin, UpdateView):
    login_url = '/login/jobseeker/'
    redirect_field_name = 'index.html'
    form_class = JobApplicationForm
    model = JobApplication
