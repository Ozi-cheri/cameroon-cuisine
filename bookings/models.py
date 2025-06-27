from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    special_request = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.date} at {self.time}"
