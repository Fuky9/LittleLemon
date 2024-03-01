from django.db import models
from django.utils import timezone

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date =  models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name} ({self.booking_date})'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title

    def showMenuItemWithPrice(self):
        return f'{self.title} : {self.price} $'

