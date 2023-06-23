from django.urls import path
from .views import (
	AppCountryListCreateView, AppCountryRetrieveUpdateDeleteView,AppCountryCreateView,AppCountryByNameView,
	AppAddressListCreateView,AppAddressRetrieveUpdateDestroyView,AppAddressCreateView,
	)

urlpatterns = [
    path('countries/', AppCountryListCreateView.as_view(), name='country-list-create'),
    path('countries/<uuid:pk>/', AppCountryRetrieveUpdateDeleteView.as_view(), name='country-retrieve-update-delete'),
    path('countries/<str:CountryName>/', AppCountryByNameView.as_view(), name='country-by-name'),
    path('countries/', AppCountryCreateView.as_view(), name='country-create'),
    path('addresses/', AppAddressListCreateView.as_view(), name='address-list-create'),
    path('addresses/<uuid:pk>/', AppAddressRetrieveUpdateDestroyView.as_view(), name='address-retrieve-update-delete'),
    path('addresses/', AppAddressCreateView.as_view(), name='address-create'),

]
