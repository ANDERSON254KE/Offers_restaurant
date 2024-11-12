from rest_framework import serializers
from .models import Offer
from accounts.serializers import RestaurantSerializer

class OfferSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        model = Offer
        fields = [
            'id',
            'restaurant',
            'title',
            'description',
            'start_date',
            'end_date',
            'is_active',
            'created_at',
            'updated_at'
        ] 