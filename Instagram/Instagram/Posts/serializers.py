from rest_framework import serializers
from .models import AppFilter, AppEffect, AppPostType, AppPost, AppPostMedia, AppPostMediaUserTag, AppPostEffect
from Users.serializers import AppUserSerializer


class AppFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFilter
        fields = ['id', 'FilterName', 'FilterDetails']

class AppEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppEffect
        fields = ['id', 'EffectName']

class AppPostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPostType
        fields = ['id', 'PostTypeName']

class AppPostSerializer(serializers.ModelSerializer):
    User = AppUserSerializer(source='PostId.UserId', read_only=True)
    class Meta:
        model = AppPost
        fields = ['id', 'User', 'Caption', 'PostTypeId']

class AppPostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPostMedia
        fields = ['id', 'PostId', 'FilterId', 'MediaFile', 'Position', 'Longitude', 'Latitude']

class AppPostMediaUserTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPostMediaUserTag
        fields = ['id', 'PostMediaId', 'UserId', 'XCoordinate', 'YCoordinate']

class AppPostEffectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPostEffect
        fields = ['id', 'EffectId', 'PostMediaId', 'Scale']
