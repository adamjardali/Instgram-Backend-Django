from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from utils.model_abstracts import Model,DateModel,CustomModel


class AppUser(CustomModel):
    _User = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255,unique=True)
    Bio = models.TextField(blank=True,null=True)
    CountryCode = models.CharField(max_length=25)
    Phone = models.CharField(max_length=25)
    ProfilePicture = models.ImageField(upload_to='profile_pictures/', blank=True,null=True)

    # def __str__(self):
    #     return f'{self.Id}'

    class Meta:
        verbose_name = 'AppUser'
        verbose_name_plural = 'AppUsers'

class AppFollower(DateModel):
    FollwingUserId = models.ForeignKey(AppUser,on_delete=models.CASCADE,related_name="Following")
    FollowedUserId = models.ForeignKey(AppUser,on_delete=models.CASCADE,related_name="Followed")

    def __str__(self):
        return f'({self.FollwingUserId},{self.FollowedUserId})'   
    
    class Meta:
        verbose_name = 'Follower'
        verbose_name_plural = 'Followers'
        unique_together = ('FollowedUserId','FollowedUserId')


