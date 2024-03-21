from django.urls import path
from driver import views

app_name='driver'

urlpatterns=[

    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.driver_signup,name='signup'),
    path('login/',views.driver_login,name='login'),
    path('requests/',views.dashboard,name='requests'),
    path('rewards/',views.dashboard,name='rewards'),
    path('logout/',views.driver_logout,name='logout'),
    path('support/',views.dashboard,name='support')

]