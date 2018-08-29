from rest_framework import serializers
from . import models
from nomadgram.users import models as user_model

class FeedUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = user_model.User
        fields = (
            'username',
            'profile_image'
        )

class CommentSerializer(serializers.ModelSerializer):

    creator = FeedUserSerializer()

    class Meta:
        model = models.Comment
        fields = {
            'id',
            'message',
            'creator'
        }

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__' # like의 필드는 creator와 image가 있다.

class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True) # 변수명이 모델에있는 related_name과 일치해야한다
    creator = FeedUserSerializer()

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'count_likes',
            'creator'
        ) # 필드의 경우 전체

