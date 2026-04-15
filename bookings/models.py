from django.db import models

class Ride(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    pickup = models.CharField(max_length=200)
    drop = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    price = models.IntegerField(null=True, blank=True)

    # 🚗 DRIVER SYSTEM
    driver_name = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.name} - {self.status}"