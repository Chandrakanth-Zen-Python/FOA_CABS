from django import forms
from django.contrib.auth.models import User
from driver.models import Drivers


class DriverUserForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():

        model=User

        fields=('username',"email",'first_name','last_name',
                'password')


class DriverProfileForm(forms.ModelForm):

    class Meta():

        model=Drivers

        fields=('city_operating','vehicle_number','mobile_number',
                'vehicle_pic','profile_pic',)