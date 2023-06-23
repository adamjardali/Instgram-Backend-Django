from django.urls import path,include
from django.contrib import admin
import Address
import Users
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api/Address/',include('Address.urls')),
    path('api/Users/',include('Users.urls')),
]