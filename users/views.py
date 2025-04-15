from rest_framework import generics, permissions
from .serializers import UserRegistrationSerializer, UserSerializer
from .models import User

# Registration view for new users
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register

# Profile view to fetch current user details
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
