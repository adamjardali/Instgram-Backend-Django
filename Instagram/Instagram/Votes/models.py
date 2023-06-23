from django.db import models
from utils.model_abstracts import Model, DateModel
from Users.models import AppUser
from Posts.models import AppPost

class AppComment(Model,DateModel):
	UserId = models.ForeignKey(AppUser,on_delete=models.CASCADE,to_field='Id')
	PostId = models.ForeignKey(AppPost,on_delete=models.CASCADE,to_field='Id')
	Comment = models.TextField()
	CommentRepliedToId = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)

	def __str__(self):
		return f'Comment Id: {self.Id}'

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'
		unique_together = ('UserId','PostId')


class AppReactionType(Model,DateModel):
	ReactionType = models.TextField(unique = True)
	ReactionEmoji = models.URLField()

	def __str__(self):
		return f'ReactionType Id: {self.Id}'

	class Meta:
		verbose_name = 'ReactionType'
		verbose_name_plural = 'ReactionsType'


class AppReaction(Model,DateModel):
	UserId = models.ForeignKey(AppUser,on_delete=models.CASCADE,to_field='Id')
	PostId = models.ForeignKey(AppPost,on_delete=models.CASCADE,to_field='Id')
	ReactionTypeId = models.ForeignKey(AppReactionType,on_delete=models.CASCADE,to_field='Id')
	
	def __str__(self):
		return f'Reaction Id: {self.Id}'

	class Meta:
		verbose_name = 'Reaction'
		verbose_name_plural = 'Reactions'
		unique_together = ('UserId','PostId')