from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    # 🔐 LOGIN SYSTEM
    path('driver/', views.driver_dashboard, name='driver_dashboard'),
    path('update-status/<int:ride_id>/<str:status>/', views.update_status, name='update_status'),
]
