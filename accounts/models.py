from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    is_restaurant_owner = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True)
    
    def has_restaurant(self):
        return hasattr(self, 'restaurant') if self.is_restaurant_owner else False

class Restaurant(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.PointField(default=Point(0.0, 0.0))
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Additional fields
    cuisine_type = models.CharField(max_length=100, blank=True)
    opening_hours = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_active_offers(self):
        return self.offer_set.filter(is_active=True)
    
    def set_location(self, latitude, longitude):
        self.location = Point(longitude, latitude)
        
    @property
    def latitude(self):
        return self.location.y if self.location else None
        
    @property
    def longitude(self):
        return self.location.x if self.location else None

@receiver(post_save, sender=User)
def create_restaurant(sender, instance, created, **kwargs):
    """
    Automatically create a restaurant profile when a restaurant owner is created
    """
    if created and instance.is_restaurant_owner:
        Restaurant.objects.create(
            owner=instance,
            name=f"{instance.username}'s Restaurant",
            description="Restaurant description goes here"
        )