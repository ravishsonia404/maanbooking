from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from django.contrib.auth.models import User

class Ride(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pickup = models.CharField(max_length=100)
    drop = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default='pending')

    # ✅ NEW FIELD
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

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
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.name} - {self.pickup} to {self.drop}"
