from django.urls import path
from . import views
# from nomadgram.images.views import (
#     ListAllImages,
#     ListAllComments,
#     ListAllLikes,
# )

app_name = "images"

urlpatterns = [
    path("all/", view=views.ListAllImages.as_view(), name="all_images"),
    path("comments/", view=views.ListAllComments.as_view(), name="all_images"),
    path("likes/", view=views.ListAllLikes.as_view(), name="all_images"),
    # url(
    #     regex=r'^all/$',
    #     view=views.ListAllImages.as_view(), 
    #     name='all_images'
    # )
]