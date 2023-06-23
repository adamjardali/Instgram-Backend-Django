from django.contrib import admin
from .models import AppUser,AppFollower
# Register your models here.

admin.site.register(AppUser)
admin.site.register(AppFollower)