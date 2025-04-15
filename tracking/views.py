# tracking/views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Package, PackageLocation
from .serializers import PackageSerializer, PackageLocationSerializer

# Endpoint for clients to create a new package (sender must be the logged in user)
class PackageCreateView(generics.CreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

# Endpoint to view a package by tracking code (anonymous access allowed)
class PackageDetailView(generics.RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'tracking_id'

# Endpoint to list packages for the logged-in user (clients viewing their own packages)
class UserPackagesListView(generics.ListAPIView):
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Package.objects.filter(sender=self.request.user)

# For drivers: update package status and location (driver must be logged in)
class PackageUpdateView(generics.UpdateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

    # You might want to add extra permission checks in production
    # so that only assigned drivers (or admins) can update the package.
