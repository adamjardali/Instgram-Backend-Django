from rest_framework import serializers
from .models import AppUser, AppFollower

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'

class AppFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFollower
        fields = '__all__'