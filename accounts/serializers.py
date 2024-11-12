from rest_framework import serializers
from .models import Restaurant, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_restaurant_owner', 'phone_number']

class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Restaurant
        fields = [
            'id', 
            'owner',
            'name', 
            'description', 
            'latitude',
            'longitude',
            'address',
            'created_at',
            'updated_at'
        ] 