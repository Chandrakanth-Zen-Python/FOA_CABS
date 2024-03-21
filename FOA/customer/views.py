from django.shortcuts import render
from driver.models import Drivers,User
from customer.forms import CustomerForm,CustomerProfileForm,RideRequestForm
from customer.models import Customers,Locations,Rides
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy

# Create your views here.

def index(request):

    return render(request,'customer/index.html')

def customer_signup(request):

    cust_form=CustomerForm()

    profile_form=CustomerProfileForm()

    if request.method=='POST':

        cust_form=CustomerForm(request.POST)

        profile_form=CustomerProfileForm(request.POST)

        print('posted:',request.POST)

        if cust_form.is_valid() and profile_form.is_valid():

            customer=cust_form.save()

            customer.set_password(customer.password)

            customer.save()

            profile=profile_form.save(commit=False)

            profile.customer=customer

            if 'profile_pic' in request.FILES:

                profile.profile_pic=request.FILES['profile_pic']
            
            profile.save()

            print('New Customer Created:',customer)

            return index(request)
    
        else:

            print(cust_form.errors)

            print(profile_form.errors)

    context_dict={'user_form':cust_form,
                  'profile_form':profile_form}
    
    return render(request,
                  'customer/signup.html',
                  context=context_dict)
            
def customer_login(request):

    context_obj={}

    if request.method=='POST':

        username=request.POST.get('username')

        password=request.POST.get('password')

        customer=authenticate(username=username,password=password)

        print('customer:',customer)

        print('profile:',Customers.objects.filter(customer=customer))

        if customer.is_authenticated and len(Customers.objects.filter(customer=customer))>0:

            login(request,customer)

            return HttpResponseRedirect(reverse('customer:home'))
        
        else:

            context_obj={'message':"Authentication Failed. Please Check Your Username and Password"}



    return render(request,'customer/login.html',context=context_obj)

def bookings(request):

    customer_obj=[x for x in Customers.objects.all() if x.customer.username==request.user.username][0]

    bookings=Rides.objects.filter(customer_name=customer_obj)

    print(bookings)

    return render(request,'customer/bookings.html',context={'bookings':bookings})

# @login_required
def home(request):


    locations=Locations.objects.all()


    return render(request,'customer/home.html',{'locations':locations})  

def page_coming_soon(request):

    return HttpResponse('Page Coming Soon!')

# @login_required
def customer_logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('index'))


# @login_required
def profile(request):

    return render(request,'customer/profile.html')


# @login_required
def book_taxi(request):

    return render(request,'customer/book_taxi.html')


# @login_required
def taxi_list(request,city): 

    print('city requested:',city)   

    drivers=Drivers.objects.filter(city_operating=city)

    print('drivers:',[x.__dict__ for x in list(drivers)])

    return render(request,
                  'customer/vehicles.html',
                  context={'drivers':drivers})


def book_ride(request,driver):

    # Get the current user's ID
    customer= request.user.username

    customer_id=request.user.id

    print('customer name:',customer)

    print('driver name:',driver)

    print(type(customer),type(driver))

    # Create the ride request form with initial data
    ride_request_form = RideRequestForm(initial={'driver_name': driver, 
                                                 'customer_name': customer})
    

    # Get the  object
    customer_obj=[x for x in Customers.objects.all() if x.customer.username==customer][0]
    driver_obj = [x for x in Drivers.objects.all() if x.driver.username==driver][0]

    print('customer_obj:',customer_obj,type(customer_obj))
    print('driver obj:',driver_obj)

    # Get the user object for the driver
    driver_user = User.objects.filter(username=driver_obj.driver).first()

    # Handle form submission
    if request.method == 'POST':
        ride_request_form = RideRequestForm(request.POST)
        
        
        if ride_request_form.is_valid():

            print('form ride:',ride_request_form.data)
            # # Save the form with the current user as the customer
            ride_request = ride_request_form.save(commit=False)
            
            ride_request.customer_name=customer_obj

            ride_request.driver_name=driver_obj

            print(ride_request.__dict__)

            ride_request.save()
            return HttpResponseRedirect(reverse('customer:bookings'))

    # Render the template with the form and context
    return render(request, 'customer/book_ride.html', {
        'ride_form': ride_request_form,
        'driver_obj': driver_obj,
        'driver_user': driver_user
    })


    



