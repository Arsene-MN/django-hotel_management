from django.db import models

class Room(models.Model):
    ROOM_TYPES = (
        ('S', 'Single'),
        ('D', 'Double'),
        ('T', 'Triple'),
    )
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=1, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.get_room_type_display()})"
