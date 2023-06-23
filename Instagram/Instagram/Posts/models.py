from django.db import models
from django.contrib.auth.models import User

from enum import Enum
from utils.model_abstracts import Model, DateModel
from Users.models import AppUser

class PostTypeChoices(Enum):
    PHOTO = 'PHOTO'
    VIDEO = 'VIDEO'
    CAROUSEL = 'CAROUSEL'
    STORIES = 'STORIES'
    REELS = 'REELS'

class AppFilter(Model,DateModel):
	FilterName = models.CharField(max_length = 255)
	FilterDetails = models.JSONField()
	def __str__(self):
		return f"Filter details: {self.FilterDetails}"

	class Meta:
		verbose_name = "Filter"
		verbose_name_plural = "Filters"

class AppEffect(Model,DateModel):
	EffectName = models.TextField()



class AppPostType(Model,DateModel):
	PostTypeName = models.CharField(max_length = 255, choices=[(choice.value, choice.name) for choice in PostTypeChoices])
	
	def __str__(self):
		return f'PostType: {self.PostType}'

	class Meta:
		verbose_name = 'PostType'
		verbose_name_plural = 'PostType'


class AppPost(Model,DateModel):
	UserId = models.ForeignKey(AppUser,on_delete = models.CASCADE,to_field = 'Id')
	Caption = models.TextField(blank=True)
	PostTypeId = models.ForeignKey(AppPostType,on_delete=models.CASCADE,to_field='Id')

	def __str__(self):
		return f'Post with Id: {self.Id} belongs to User with Id: {self.UserId}'

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

class AppPostMedia(Model,DateModel):
	PostId = models.ForeignKey(AppPost,on_delete=models.CASCADE,to_field='Id')
	FilterId = models.ForeignKey(AppFilter,on_delete=models.CASCADE,to_field='Id')
	MediaFile = models.URLField(null = True)
	Position = models.IntegerField()
	Longitude = models.IntegerField()
	Latitude = models.IntegerField()

	def __str__(self):
		return f'PostMedia Id: {self.Id}'

	class Meta:
		verbose_name = 'PostMedia'
		verbose_name_plural = 'PostsMedia'
		unique_together = ('FilterId','PostId')

class AppPostMediaUserTag(DateModel):
	PostMediaId = models.ForeignKey(AppPostMedia,on_delete=models.CASCADE,to_field='Id')
	UserId = models.ForeignKey(AppUser,on_delete=models.CASCADE,to_field='Id')
	XCoordinate = models.IntegerField()
	YCoordinate = models.IntegerField()

	def __str__(self):
		return f'User Id: {self.UserId}, Post Id: {self.PostMediaId}'

	class Meta:
		verbose_name = 'Tag'  		
		verbose_name_plural = 'Tags'
		unique_together = ('PostMediaId','UserId')

class AppPostEffect(DateModel):
	EffectId = models.ForeignKey(AppEffect,on_delete=models.CASCADE,to_field = 'Id')
	PostMediaId = models.ForeignKey(AppPostMedia,on_delete=models.CASCADE,to_field='Id')
	Scale = models.TextField()

	def __str__(self):
		return f'Effect Id: {self.EffectId}, PostMediaId: {self.PostMediaId}'

	class Meta:
		verbose_name = 'PostEffect'
		verbose_name_plural = 'PostEffects'
		unique_together = ('EffectId','PostMediaId')	






