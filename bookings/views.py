from django.shortcuts import render, redirect
from .forms import RideForm
from django.shortcuts import render, get_object_or_404
from .models import Ride


# 👤 USER BOOK RIDE
def home(request):
    form = RideForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            ride = form.save(commit=False)

            ride.status = 'pending'
            ride.price = None  # driver sets later

            ride.save()

            return render(request, 'success.html', {'ride': ride})

    return render(request, 'home.html', {'form': form})


# 🚗 DRIVER DASHBOARD
def driver_dashboard(request):
    rides = Ride.objects.all().order_by('-id')  # later filter by driver

    return render(request, 'driver_dashboard.html', {'rides': rides})
def update_status(request, ride_id, status):
    ride = get_object_or_404(Ride, id=ride_id)
    ride.status = status
    ride.save()

    return redirect('driver_dashboard')

# 🚗 ACCEPT RIDE
def accept_ride(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    ride.status = 'accepted'
    ride.save()
    return redirect('driver_dashboard')


# ❌ REJECT RIDE
def reject_ride(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    ride.status = 'rejected'
    ride.save()
    return redirect('driver_dashboard')


# 🛠 ADMIN DASHBOARD
def admin_dashboard(request):
    rides = Ride.objects.all()
    return render(request, 'admin_dashboard.html', {'rides': rides})
