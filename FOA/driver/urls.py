from django.urls import path
from driver import views

app_name='driver'

urlpatterns=[

    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.driver_signup,name='signup'),
    path('login/',views.driver_login,name='login'),
    path('requests/',views.rides,name='requests'),
    path('ride_status/<str:book_id>/<str:status_change>/',views.ride_status_update,name='ride_status'),
    path('payment_status/<str:book_id>/<str:payment_status>/',views.payment_status,name='payment_status'),
    path('rewards/',views.dashboard,name='rewards'),
    path('logout/',views.driver_logout,name='logout'),
    path('support/',views.dashboard,name='support')

]