from rest_framework.test import APIClient, APITestCase
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer

client = APIClient()

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
