from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class ListAllImages(APIVIEW):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)
        # 그냥 시리얼 라이즈는 단수이다 mant=True를 통해 알려준다
        return Response(data=serializer.data)
