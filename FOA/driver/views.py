from django.shortcuts import render
from driver.forms import DriverUserForm,DriverProfileForm
from driver.models import Drivers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy


# Create your views here.
# @login_required(login_url=reverse('driver:login'))
def dashboard(request):

    return render(request,'driver/dashboard.html',{})

def driver_signup(request):

    driver_form=DriverUserForm()

    profile_form=DriverProfileForm()

    if request.method=='POST':

        driver_form=DriverUserForm(request.POST)

        profile_form=DriverProfileForm(request.POST)

        print('posted:',request.POST)

        if driver_form.is_valid() and profile_form.is_valid():

            driver=driver_form.save()

            driver.set_password(driver.password)

            driver.save()

            profile=profile_form.save(commit=False)

            profile.driver=driver

            if 'profile_pic' in request.FILES:

                profile.profile_pic=request.FILES['profile_pic']
            
            if 'vehicle_pic' in request.FILES:

                profile.vehicle_pic=request.FILES['vehicle_pic']
            
            profile.save()

            print('New driver Created:',driver)

            return dashboard(request)
    
        else:

            print(driver_form.errors)

            print(profile_form.errors)

    context_dict={'user_form':driver_form,
                  'profile_form':profile_form}
    
    return render(request,
                  'customer/signup.html',
                  context=context_dict)
     
def driver_login(request):

    context_obj={}

    if request.method=='POST':

        username=request.POST.get('username')

        password=request.POST.get('password')

        driver=authenticate(username=username,password=password)

        print('driver:',driver)

        print('profile:',Drivers.objects.filter(driver=driver))

        if driver.is_authenticated and len(Drivers.objects.filter(driver=driver))>0:

            login(request,driver)

            return HttpResponseRedirect(reverse('driver:dashboard'))
        
        else:

            context_obj={'message':"Authentication Failed. Please Check Your Username and Password"}


    return render(request,'customer/login.html',context_obj)


# @login_required(login_url=reverse('driver:login'))
def driver_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('index'))