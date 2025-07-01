from django.shortcuts import render, redirect
from .forms import BookingForm

def home(request):
    return render(request, 'bookings/home.html')

def booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'bookings/booking_success.html')

def menu(request):
    return render(request, 'bookings/menu.html')

def login_view(request):
    return render(request, 'bookings/login.html')

def signup_view(request):
    return render(request, 'bookings/signup.html')

def contact_view(request):
    return render(request, 'bookings/contact.html')
