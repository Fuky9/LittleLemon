from rest_framework.serializers import ModelSerializer
from .models import Booking, Menu

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        extra_kwargs = {
            'price': {'min_value': 1},
            'inventory': {'min_value': 1},
        }

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {
            'no_of_guests': {'min_value': 1},
        }