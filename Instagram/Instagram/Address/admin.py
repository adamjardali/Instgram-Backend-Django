from django.contrib import admin
from .models import AppCountry, AppAddress,AppUserAddress
# Register your models here.

admin.site.register(AppCountry)
admin.site.register(AppAddress)
admin.site.register(AppUserAddress)