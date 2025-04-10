# tracking/serializers.py
from rest_framework import serializers
from .models import Package, PackageLocation

class PackageLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageLocation
        fields = ('id', 'latitude', 'longitude', 'timestamp', 'is_current')

class PackageSerializer(serializers.ModelSerializer):
    locations = PackageLocationSerializer(many=True, read_only=True)
    tracking_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Package
        fields = ('id', 'tracking_id', 'sender', 'recipient_name', 'recipient_email',
                  'origin_address', 'destination_address', 'assigned_driver', 'status',
                  'created_at', 'locations')
        read_only_fields = ('sender', 'created_at',)
