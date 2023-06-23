from rest_framework import serializers
from .models import AppCountry, AppAddress, AppUserAddress

class AppCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppCountry
        fields = ['CountryName']

        
class AppAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppAddress
        fields = ['UnitNumber', 'StreetNumber', 'AddressLineOne', 'AddressLineTwo', 'City', 'Region', 'PostalCode', 'CountryId']

class AppUserAddressSerializer(serializers.ModelSerializer):
    Address = serializers.PrimaryKeyRelatedField(queryset=AppAddress.objects.all(), allow_null=True)

    class Meta:
        model = AppUserAddress
        fields = ['AppUserId', 'Address']