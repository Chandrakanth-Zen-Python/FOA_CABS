from django.contrib import admin
from customer.models import Customers,Rides,Locations

# Register your models here.

admin.site.register(Customers)
admin.site.register(Rides)
admin.site.register(Locations)
