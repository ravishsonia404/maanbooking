from django.db import models
from django.contrib.auth.models import User


class Ride(models.Model):
    # 👤 Customer Details
    name = models.CharField(max_length=100)
    email = models.EmailField()

    # 📍 Ride Details
    pickup = models.CharField(max_length=100)
    drop = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    # 💰 Price (decided by driver)
    price = models.IntegerField(null=True, blank=True)

    # 👨‍✈️ Driver (linked with login system)
    driver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # 🚦 Status
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # 📅 Created time (for sorting)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.pickup} to {self.drop}"
