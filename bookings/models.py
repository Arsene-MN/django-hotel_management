# bookings/models.py
from django.db import models
from rooms.models import Room
from guests.models import Guest

class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for room in self.rooms.all():
            room.available = False
            room.save()

    def __str__(self):
        return f"Booking for {self.guest.first_name} {self.guest.last_name} from {self.check_in_date} to {self.check_out_date}"
