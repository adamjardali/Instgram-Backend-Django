from django.db import models
from django_countries.fields import CountryField


from utils.model_abstracts import Model, DateModel
from Users.models import AppUser


class AppCountry(Model,DateModel):
	CountryName = CountryField(unique = True)

	def __str__(self):
		return f'{self.CountryName}'
	
	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'
		ordering = ['-CountryName']


class AppAddress(Model,DateModel):
	UnitNumber = models.CharField(max_length=255)
	StreetNumber = models.CharField(max_length=255)
	AddressLineOne = models.CharField(max_length=255)
	AddressLineTwo = models.CharField(max_length=255,blank=True,null=True)
	City = models.CharField(max_length=255,blank=True,null=True)
	Region = models.CharField(max_length=255,blank=True,null=True)
	PostalCode = models.CharField(max_length=255)
	CountryId = models.ForeignKey(AppCountry,on_delete=models.CASCADE,to_field='Id')

	def __str__(self):
		return f'Address Id: {self.Id}'

	class Meta:
		verbose_name = 'Address'
		verbose_name_plural = 'Addresses'


class AppUserAddress(Model,DateModel):
	AppUserId = models.ForeignKey(AppUser,on_delete=models.CASCADE,to_field='Id')
	AddressId = models.ForeignKey(AppAddress,on_delete=models.CASCADE,to_field='Id')

	def __str__(self):
		return f'User with Id: {self.Id} has Address Id: {self.Id}'

	class Meta:
		verbose_name = 'UserAddress'
		verbose_name_plural = 'UserAddresses'	