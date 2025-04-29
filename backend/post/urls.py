from django.urls import path
from post.views import create_post,get_image,delete_post,list_all_posts,post_from_followeduser,post_from_specificuser,retrieve_single_post

urlpatterns = [
    path("create_post/",create_post,name="create_post"),
    path('<str:post_id>/image/', get_image, name='get_image'),
    path('<str:post_id>/delete_post/',delete_post,name='delete_post'),
    # path('<str:post_id>/like_post/',like_post,name='delete_post'),
    path('list_all_posts/',list_all_posts,name='list_all_posts'),
    path('post_from_followeduser/',post_from_followeduser,name='post_from_followeduser'),
    path('<str:user_id>/post_from_specificuser/',post_from_specificuser,name='post_from_specificuser'),
    path('<str:post_id>/retrieve_single_post/',retrieve_single_post,name='post_from_specificuser'),
]
