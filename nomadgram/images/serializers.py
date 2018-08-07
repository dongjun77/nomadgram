from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__' # like의 필드는 creator와 image가 있다.


class ImageSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True) # 변수명이 모델에있는 related_name과 일치해야한다
    likes = LikeSerializer(many=True)

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes',
        ) # 필드의 경우 전체

