from django.urls import path
from post.views import create_post,get_image,delete_post

urlpatterns = [
    path("create_post/",create_post,name="create_post"),
    path('<str:post_id>/image/', get_image, name='get_image'),
    path('<str:post_id>/delete_post/',delete_post,name='delete_post')
]
