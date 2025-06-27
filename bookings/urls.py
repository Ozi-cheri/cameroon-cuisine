from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('menu/', views.menu, name='menu'),
    path('book/', views.booking_form, name='booking_form'),  # Booking form
    path('success/', views.booking_success, name='booking_success'),  # Booking success page
]
