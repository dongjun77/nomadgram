from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer):

    class Meta:
        model = models.Image
        fields = '__all__' # 필드의 경우 전체

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.Serializer):

    class Meta:
        model = models.Like
        fields = '__all__'
