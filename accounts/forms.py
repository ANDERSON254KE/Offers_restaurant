from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Restaurant

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_restaurant_owner')

class RestaurantForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_restaurant_owner')

class RestaurantLocationForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'id': 'address-input'}))
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'address', 'cuisine_type', 'opening_hours'] 