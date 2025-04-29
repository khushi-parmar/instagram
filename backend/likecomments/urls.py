from django.urls import path
from likecomments.views import like_post,list_of_likes,check_like

urlpatterns = [
    path('<str:post_id>/like_post/',like_post,name="like_post"),
    path('<str:post_id>/list_of_likes/',list_of_likes,name="list_of_likes"),
    path('<str:post_id>/check_like/',check_like,name="check_like"),
]
