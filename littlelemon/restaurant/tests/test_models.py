from rest_framework.test import APITestCase
from restaurant.models import Menu

class MenuTest(APITestCase):
    # Creating test object for all tests
    @classmethod
    def setUpTestData(cls):
        Menu.objects.create(title='Ice cream', price=80, inventory=100)

    # Testing if __str__() works properly
    def test_menu_item(self):
        item = Menu.objects.get(id=1)
        self.assertEqual(str(item), 'Ice cream')

    # Testing model function to show title and price
    def test_ShowMenuItemWithPrice(self):
        item = Menu.objects.get(id=1)
        self.assertEqual(Menu.showMenuItemWithPrice(item), 'Ice cream : 80.00 $')
