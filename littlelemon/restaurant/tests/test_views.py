from rest_framework.test import APITestCase
from django.test import TestCase
from restaurant.models import Menu, Booking
from django.urls import reverse
from restaurant.serializers import MenuSerializer, BookingSerializer
from django.utils import timezone
from django.contrib.auth.models import User

class IndexViewTest(TestCase):

    def test_template_response(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'index.html')

class MenuItemViewSetTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        # Creating 10 Menu instances
        number_of_instances = 10

        for menu_id in range(number_of_instances):
            Menu.objects.create(
                title=f'Food {menu_id}',
                price= menu_id,
                inventory= 10 + menu_id,
            )

    def test_list_view(self):
        # Test by URL
        response_by_url = self.client.get('/restaurant/menu/')
        self.assertEqual(response_by_url.status_code, 200)

        # Test by name
        response_by_name = self.client.get(reverse('menu-list'))
        self.assertEqual(response_by_name.status_code, 200)

        # Test if view shows all data (works only for 10 records because of pagination set to 10)
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        serialized_data = serializer.data
        self.assertEqual(response_by_name.data["results"], serialized_data)

    def test_retrieve_view(self):
        ''''''
        # Test by name
        response = self.client.get(reverse('menu-retrieve', args=[7]))
        self.assertEqual(response.status_code, 200)

        # Test by URL
        response_by_url = self.client.get('/restaurant/menu/7')
        self.assertEqual(response_by_url.status_code, 200)

        # Test if the view shows data
        item = Menu.objects.get(id='7')
        serializer = MenuSerializer(item)
        self.assertEqual(response.data, serializer.data)

class BookingViewSetTest(APITestCase):
    '''Class for testing BokkingViewSet'''
    @classmethod
    def setUpTestData(cls):
        '''Creating 10 Booking instances and user for testing'''
        number_of_instances = 10
        for booking_id in range(number_of_instances):
            Booking.objects.create(
                name = f'Lukas{booking_id}',
                no_of_guests = booking_id,
                booking_date = timezone.now()
            )

        test_user = User.objects.create_user(username='Lukas', password='1234')
        test_user.save()


    def test_list_view_not_login(self):
        '''Testing if authentication works'''

        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, 401)


    def test_list_view_login(self):
        '''Testing if authenticated user get 200 and if endpoint shows data'''

        # simulating logged in user
        self.client.login(username='Lukas', password='1234')
        # URL
        response = self.client.get('/restaurant/booking/tables/')
        self.assertEqual(response.status_code, 200)

        # Name
        response_by_name = self.client.get(reverse('booking-list')) # By default when using router basename is created from queryset and list
        self.assertEqual(response_by_name.status_code, 200)

        # Data
        serializer = BookingSerializer(Booking.objects.all(), many=True)
        self.assertEqual(response.data['results'], serializer.data)


    def test_retrieve_view_login(self):
        '''Testing if authenticated user get 200 and if endpoint shows data'''

        # simulating logged in user
        self.client.login(username='Lukas', password='1234')

        # URL
        response = self.client.get('/restaurant/booking/tables/5/')
        self.assertEqual(response.status_code, 200)

        # Name
        response_by_name = self.client.get(reverse('booking-detail', args=[5])) # By default when using router basename is created from queryset and detail
        self.assertEqual(response_by_name.status_code, 200)

        # Data
        item = Booking.objects.get(id=5)
        serializer = BookingSerializer(item)
        self.assertEqual(response.data, serializer.data)
