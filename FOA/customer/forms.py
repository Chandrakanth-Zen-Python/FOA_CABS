from django import forms
from django.contrib.auth.models import User
from customer.models import Customers,Rides


class CustomerForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model=User

        fields=('username',"email",'first_name','last_name',
                'password')


class CustomerProfileForm(forms.ModelForm):

    class Meta():

        model=Customers

        fields=('profile_pic',)


class RideRequestForm(forms.ModelForm):

    # driver=forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta():

        model=Rides

        fields=('journey_start_point','journey_end_point',)






