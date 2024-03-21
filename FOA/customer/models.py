from django.db import models
from django.contrib.auth.models import User
from driver.models import Drivers
from django.utils import timezone
import uuid
from datetime import datetime

# Create your models here.

class Customers(models.Model):

    customer = models.OneToOneField(User,on_delete=models.CASCADE)

    profile_pic=models.ImageField(
        upload_to='customer/profile_pic/',
        blank=True
        )

    def __str__(self):

        return self.customer.username
    

class Locations(models.Model):

    city=models.CharField(unique=True,max_length=30)

    state=models.CharField(max_length=30)

    # location_pic=models.ImageField(upload_to='locations/',
    #                                default='locations/default_location.jpg')

    def __str__(self):

        return self.city



class Rides(models.Model):

    book_id = models.CharField(primary_key=True,
                               default=uuid.uuid4,
                               editable=False,max_length=100)

    customer_name=models.ForeignKey(Customers,on_delete=models.DO_NOTHING)

    driver_name=models.ForeignKey(Drivers,on_delete=models.DO_NOTHING)

    hours_travelled=models.FloatField(verbose_name='Hours Travelled',default=0)

    journey_start_point=models.ForeignKey(Locations,models.DO_NOTHING,
                                          verbose_name='Journey Start Point',
                                         max_length=100,
                                         related_name='journey_start_location')

    journey_end_point=models.ForeignKey(Locations,models.DO_NOTHING,
                                        verbose_name='Journey End Point',
                                       max_length=100,
                                       related_name='journey_end_location')
    
    journey_start_time=models.DateTimeField(verbose_name='Journey Start Time',default=timezone.now)

    journey_end_time=models.DateTimeField(verbose_name='Journey End Time',default=timezone.now)

    payment_amount=models.FloatField(default=0)

    payment_status_choices=(
        ('paid',"Paid"),
        ('not_paid','Not Paid'),
        ('refund','Refunded')
    )

    payment_status=models.CharField(default='not_paid',
                                    choices=payment_status_choices,
                                    max_length=10)
    
    ride_status_choices=(
        ('booked','Booked'),
        ('started','Started'),
        ('completed','Completed'),
        ('cancelled','Cancelled')
    )
    ride_status=models.CharField(default='booked',
                                 choices=ride_status_choices,
                                 max_length=10)

    createdAt=models.DateTimeField(auto_now_add=True)

    rating_choices=(
        ('poor',1),
        ('below average',2),
        ('average',3),
        ('above average',4),
        ('good',5)
                    )

    rating=models.IntegerField(choices=rating_choices,null=True)


    def __str__(self):

        return self.book_id













