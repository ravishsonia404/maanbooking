from django.contrib import admin
from django.urls import path
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    # 🚗 driver system
    path('driver/', views.driver_dashboard, name='driver_dashboard'),
    path('accept/<int:ride_id>/', views.accept_ride),
    path('reject/<int:ride_id>/', views.reject_ride),

    # 🛠 admin panel
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]