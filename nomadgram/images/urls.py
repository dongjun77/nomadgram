from django.urls import path
from . import views
# from nomadgram.images.views import (
#     ListAllImages,
#     ListAllComments,
#     ListAllLikes,
# )

app_name = "images"

urlpatterns = [
    path("", view=views.Feed.as_view(), name='feed'),
    # path("<int:id>/like/", view=views.LikeImage.as_view(), name='like_image'),
    # path("all/", view=views.ListAllImages.as_view(), name="all_images"),
    # path("comments/", view=views.ListAllComments.as_view(), name="all_images"),
    # path("likes/", view=views.ListAllLikes.as_view(), name="all_images"),
    # url(
    #     regex=r'^all/$',
    #     view=views.ListAllImages.as_view(), 
    #     name='all_images'
    # )
]