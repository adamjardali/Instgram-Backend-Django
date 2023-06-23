from rest_framework import serializers

# from api.serializers import UserPublicSerializer
from .models import AppComment, AppReactionType, AppReaction
from Posts.model import AppPost
from Users.models import AppUser

class AppCommentSerializer(serializers.ModelSerializer):
    Post = serializers.PrimaryKeyRelatedField(queryset=AppPost.objects.filter(id = PostId), many=False, allow_null=True, required=False)
    ParentComment = serializers.PrimaryKeyRelatedField(queryset=AppComment.objects.filter(id = CommentRepliedToId), many=False, allow_null=True, required=False)

    class Meta:
        model = AppComment
        fields = ['UserId','Post','Comment','ParentComment']



class AppReactionTypeSerializer(serializers.ModelSerializer):


	class Meta:
		model = AppReactionType
		fields = ['ReactionType','ReactionEmoji']


class AppReactionSerializer(serializers.ModelSerializer):
    Post = serializers.PrimaryKeyRelatedField(queryset=AppPost.objects.filter(id = PostId), many=False, allow_null=True, required=False)
    Post = serializers.PrimaryKeyRelatedField(queryset=AppUser.objects.filter(id = UserId), many=False, allow_null=True, required=False)


	class Meta:
		model = AppReaction
		fields = ['User','Post','ReactionTypeId']


