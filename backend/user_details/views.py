from django.shortcuts import render
from rest_framework.decorators import api_view
from backend.decorators import jwt_required
from .models import Follow
from authentication.models import User
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# view user profile
# Edit/update profile
# Upload/change profile picture

@api_view(["POST"])
@jwt_required
def follow_user(request,user_id):
    # if followw.follower==request.user and followw.following 
    
    target_user=User.objects.get(_id=user_id)
    follow=Follow.objects.filter(follower=request.user,following=target_user).first()
    
    if follow:
        follow.delete()
        return Response({"message":"unfollowed successfully"},status=status.HTTP_200_OK)
    else:
        Follow.objects.create(
        follower=request.user,
        following= target_user)
        return Response({"message":"followed"},status=status.HTTP_201_CREATED)
    
 
@api_view(["GET"])
@jwt_required   
def list_followers(request):
    followers=Follow.objects.filter(following=request.user)
    follower_list=[{"follower_username":f.follower.username}for f in followers]
    return Response({"follower_list":follower_list},status=status.HTTP_200_OK)
   

@api_view(["GET"])
@jwt_required
def list_following(request):
       following=Follow.objects.filter(follower=request.user)
       following_list=[{"following_list":f.following.username} for f in following]
       return Response({"following_list":following_list},status=status.HTTP_200_OK)
    
    