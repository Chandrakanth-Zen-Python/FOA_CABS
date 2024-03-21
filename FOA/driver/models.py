from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Drivers(models.Model):

    driver=models.OneToOneField(User,on_delete=models.CASCADE)

    vehicle_number=models.CharField(verbose_name='Vehicle Registration Number',
                                    unique=True,max_length=20)
    
    city_operating=models.CharField(max_length=20,null=False)

    vehicle_pic=models.ImageField(verbose_name='Upload Your Vehicle Photo',
                                  upload_to='driver/vehicle',
                                  blank=True)
    
    profile_pic=models.ImageField(verbose_name='Profile Picture',
                                  upload_to='driver/profile_pic',
                                  blank=True)
    
    mobile_number=models.CharField(verbose_name='Mobile Number',
                                   default='',
                                   max_length=20)
    
    createdAt=models.DateTimeField(auto_now_add=True)


    def __str__(self): 

        return self.driver.username
