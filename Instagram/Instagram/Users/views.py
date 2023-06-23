from rest_framework import generics
from .models import AppUser, AppFollower
from .serializers import AppUserSerializer, AppFollowerSerializer

class AppUserListCreateView(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class AppUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class AppFollowerListCreateView(generics.ListCreateAPIView):
    queryset = AppFollower.objects.all()
    serializer_class = AppFollowerSerializer

class AppFollowerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppFollower.objects.all()
    serializer_class = AppFollowerSerializer
