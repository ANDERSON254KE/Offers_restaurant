from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.shortcuts import render
from accounts.models import Restaurant

def search_restaurants(request):
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lng')
    radius = request.GET.get('radius', 5)  # Default 5km radius
    
    if latitude and longitude:
        user_location = Point(float(longitude), float(latitude))
        restaurants = Restaurant.objects.filter(
            location__distance_lte=(user_location, D(km=radius))
        ).distance(user_location).order_by('distance')
    else:
        restaurants = Restaurant.objects.all()
        
    return render(request, 'offers/search_restaurants.html', {
        'restaurants': restaurants
    }) 