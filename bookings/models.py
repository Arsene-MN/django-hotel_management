# bookings/models.py
from django.db import models
from guests.models import Guest  # Ensure you have a Guest model
from rooms.models import Room  # Ensure you have a Room model

class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)  # Change to ManyToManyField
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f"Booking for {self.guest.name} from {self.check_in_date} to {self.check_out_date}"
