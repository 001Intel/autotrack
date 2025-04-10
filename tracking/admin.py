from django.contrib import admin
from .models import Package, PackageLocation

admin.site.register(Package)
admin.site.register(PackageLocation)
