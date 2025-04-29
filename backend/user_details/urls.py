from django.urls import path
from user_details.views import follow_user,list_followers,list_following

urlpatterns = [
    path('<str:user_id>/follow_user/',follow_user,name='follow_user'),
    path('list_followers/',list_followers,name='list_followers'),
    path('list_following/',list_following,name='list_following'),
]

