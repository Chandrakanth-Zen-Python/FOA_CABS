from django.shortcuts import render
from driver.forms import DriverUserForm,DriverProfileForm
from driver.models import Drivers
from customer.models import Rides
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.db.models import Count, Sum, Case, When, IntegerField


# Create your views here.
# @login_required(login_url=reverse('driver:login'))
def dashboard(request):

    context={'driver_stats':{'amount_collected':10000,
                             "num_rides_completed":10,
                             "num_rides_received":20}}
    
    try:
    
        driver_obj=[x for x in Drivers.objects.all() if x.driver.username==request.user.username][0]
    
    except IndexError:  

        logout(request)      

        return driver_login(request)
    
    # Group by driver_id, count number of trips, and sum distance_traveled
    result = Rides.objects.filter(driver_name=driver_obj).values('driver_name').annotate(
        num_rides_received=Count('book_id'),
        amount_collected=Sum('payment_amount'),
        num_rides_completed=Count(
            Case(
                When(ride_status='completed', then=1),
                output_field=IntegerField()
            )
        )
    )

   

    context={"driver_stats":result[0]}

    print(context)

    return render(request,'driver/dashboard.html',context=context)


def rides(request):

    driver_obj=[x for x in Drivers.objects.all() if x.driver.username==request.user.username][0]

    rides=Rides.objects.filter(driver_name=driver_obj)

    print(rides)

    return render(request,
                  'driver/booking_requests.html',
                  context={"bookings":rides})


def ride_status_update(request,book_id,status_change):

    ride=Rides.objects.get(book_id=book_id)

    ride.ride_status=status_change

    ride.save()

    return HttpResponseRedirect(reverse('driver:requests'))


def payment_status(request,book_id,payment_status):

    ride=Rides.objects.get(book_id=book_id)

    ride.payment_status=payment_status

    ride.save()

    return HttpResponseRedirect(reverse('driver:requests'))




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