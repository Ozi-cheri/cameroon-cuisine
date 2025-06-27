from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'guests', 'date', 'time')
    list_filter = ('date', 'guests')
    search_fields = ('full_name', 'email', 'phone')
