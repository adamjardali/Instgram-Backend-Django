from rest_framework import generics
from rest_framework.exceptions import NotFound

from .models import AppCountry, AppAddress
from .serializers import AppCountrySerializer, AppAddressSerializer



'''
	Get a Country By Name
'''

class AppCountryByNameView(generics.RetrieveAPIView):
    queryset = AppCountry.objects.all()
    serializer_class = AppCountrySerializer
    lookup_field = 'CountryName'

''' 
	Create A New Country
'''

class AppCountryCreateView(generics.CreateAPIView):
    queryset = AppCountry.objects.all()
    serializer_class = AppCountrySerializer

''' 
	List All Created Countreis
'''

class AppCountryListCreateView(generics.ListCreateAPIView):
    queryset = AppCountry.objects.all()
    serializer_class = AppCountrySerializer

''' 
	Get/UPDATE/DELETE A Country By Id
'''

class AppCountryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppCountry.objects.all()
    serializer_class = AppCountrySerializer

'''
	Create A New Address
'''

class AppAddressCreateView(generics.CreateAPIView):
    queryset = AppAddress.objects.all()
    serializer_class = AppAddressSerializer

''' 
	List All Addresses
'''

class AppAddressListCreateView(generics.ListCreateAPIView):
    queryset = AppAddress.objects.all()
    serializer_class = AppAddressSerializer

''' 
	GET/UPDATE/DELETE An Address
'''

class AppAddressRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppAddress.objects.all()
    serializer_class = AppAddressSerializer
