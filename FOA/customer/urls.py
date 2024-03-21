from django.urls import path
from customer import views

app_name='customer'



urlpatterns=[
    path('profile/',views.profile,name='customer_profile'),
    path('login/',views.customer_login,name='customer_login'),
    path('signup/',views.customer_signup,name='customer_signup'),
    path('home/',views.home, name='home'),
    path('taxi_list/<str:city>',views.taxi_list, name='taxi_list'),
    path('bookings/',views.bookings, name='bookings'),
    path('rewards/',views.page_coming_soon, name='rewards'),
    path('support/',views.page_coming_soon, name='support'),
    path('logout/',views.customer_logout, name='logout'),
    path('book_ride/<str:driver>',views.book_ride,name='book_ride')
]