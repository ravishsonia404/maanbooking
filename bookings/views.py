from django.shortcuts import render, redirect
from .forms import RideForm
from django.shortcuts import render, get_object_or_404
from .models import Ride


# 👤 USER BOOK RIDE
from datetime import datetime

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pickup = request.POST.get('pickup')
        drop = request.POST.get('drop')
        date = request.POST.get('date')
        time = request.POST.get('time')

        # Convert date safely
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        except:
            return render(request, 'home.html', {'error': 'Invalid date format'})

        try:
            Ride.objects.create(
                name=name,
                email=email,
                pickup=pickup,
                drop=drop,
                date=date_obj,
                time=time,
                status='pending'
            )
        except Exception as e:
            return render(request, 'home.html', {'error': str(e)})

        return render(request, 'success.html', {
            'name': name,
            'pickup': pickup,
            'drop': drop,
            'date': date,
            'time': time,
        })

    return render(request, 'home.html')

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
