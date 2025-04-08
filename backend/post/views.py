from django.shortcuts import render
from rest_framework.decorators import api_view
from post.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from backend.decorators import jwt_required
from post.models import Post
from django.http import FileResponse
from rest_framework.response import Response

# Create your views here.

@api_view(["POST"])
@jwt_required
def create_post(request):
    serializer=PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user_id=request.user)
        return Response({
            "message":"you image is posted",
            "post":serializer.data
        },status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_image(request, post_id):                       
    post = Post.objects.get(_id=post_id)
    if post.image:
        return FileResponse(post.image, content_type='image/jpeg')
    return Response({"error": "No image found"}, status=404)

@api_view(["DELETE"])
@jwt_required
def delete_post(request,post_id):
    post=Post.objects.get(_id=post_id)
    post.delete()
    
    return Response({"message":"post deleted successfully"},status=status.HTTP_200_OK)
# return Response({"error":"not deleted"},status=status.HTTP_400_BAD_REQUEST)