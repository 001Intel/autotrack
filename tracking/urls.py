# tracking/urls.py
from django.urls import path
from .views import PackageCreateView, PackageDetailView, UserPackagesListView, PackageUpdateView

urlpatterns = [
    path('create/', PackageCreateView.as_view(), name='package-create'),
    path('my-packages/', UserPackagesListView.as_view(), name='user-packages'),
    path('<uuid:tracking_id>/', PackageDetailView.as_view(), name='package-detail'),
    path('update/<int:pk>/', PackageUpdateView.as_view(), name='package-update'),
]
