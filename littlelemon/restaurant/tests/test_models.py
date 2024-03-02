from rest_framework.test import APITestCase
from restaurant.models import Menu, Booking
from django.utils import timezone

class MenuTest(APITestCase):
    # Creating test object for all tests
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(title='Ice cream', price=80, inventory=100)

    # Testing if __str__() works properly
    def test_menu_item_str(self):
        item = Menu.objects.get(id=1)
        self.assertEqual(str(item), 'Ice cream')

    # Testing model function to show title and price
    def test_ShowMenuItemWithPrice(self):
        item = Menu.objects.get(id=1)
        self.assertEqual(Menu.showMenuItemWithPrice(item), 'Ice cream : 80.00 $')

class BookingTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Booking.objects.create(name='Lukas', no_of_guests=6, booking_date=timezone.now())

    def test_booking_str(self):
       booking = Booking.objects.get(id=1)
       self.assertEqual(str(booking), f'Lukas ({booking.booking_date})')
