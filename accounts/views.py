from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, RestaurantLocationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def restaurant_edit(request):
    if not request.user.is_restaurant_owner:
        return redirect('profile')
        
    restaurant = getattr(request.user, 'restaurant', None)
    if request.method == 'POST':
        form = RestaurantLocationForm(request.POST, instance=restaurant)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = request.user
            restaurant.set_location(
                form.cleaned_data['latitude'],
                form.cleaned_data['longitude']
            )
            restaurant.save()
            return redirect('profile')
    else:
        initial = {}
        if restaurant:
            initial = {
                'latitude': restaurant.latitude,
                'longitude': restaurant.longitude
            }
        form = RestaurantLocationForm(instance=restaurant, initial=initial)
    
    return render(request, 'accounts/restaurant_form.html', {'form': form}) 