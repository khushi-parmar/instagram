from django.shortcuts import render
from rest_framework.decorators import api_view
from backend.decorators import jwt_required
from .models import Like
from rest_framework.response import Response 
from django.http import FileResponse
from rest_framework import status
from .serializers import UserSerializer
# Create your views here.

@api_view(["POST"])
@jwt_required
def like_post(request,post_id):
    like=Like.objects.filter(liked_by_whom=request.user).first()
    if like:
        like.delete()
        return Response({"message":"unlike successfully"},status=status.HTTP_200_OK)
    else:
        Like.objects.create(
            post_id=post_id,
            liked_by_whom=request.user
        )
        return Response({"message":"liked"},status=status.HTTP_201_CREATED)
    
@api_view(["GET"])
@jwt_required
def list_of_likes(request,post_id):
    likes=Like.objects.filter(post_id=post_id)
    liked_users=[like.liked_by_whom for like in likes]
    
    serializer=UserSerializer(liked_users,many=True)
    data={
        "likes_count":likes.count(),
        "liked_users":serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)

@api_view(["GET"])
@jwt_required
def check_like(request,post_id):
    like=Like.objects.filter(post_id=post_id,liked_by_whom=request.user)
    if like:
        return Response({"message":"liked"},status=status.HTTP_200_OK)
    else:
        return Response({"message":"not liked"},status=status.HTTP_200_OK)