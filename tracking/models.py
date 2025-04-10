from django.db import models
from users.models import User
import uuid

class Package(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('picked_up', 'Picked Up'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    tracking_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_packages')
    recipient_name = models.CharField(max_length=255)
    recipient_email = models.EmailField()
    origin_address = models.TextField()
    destination_address = models.TextField()
    assigned_driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Package {self.tracking_id} to {self.recipient_name}"

class PackageLocation(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='locations')
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.package.tracking_id} @ {self.latitude},{self.longitude}"
