from django.shortcuts import render
from rest_framework.decorators import api_view
from post.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from backend.decorators import jwt_required
from post.models import Post,Like,User
from django.http import FileResponse
from rest_framework.response import Response
from user_details.models import Follow

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
    if post.user != request.user:
        return Response({"message": "You are not allowed to delete this post."}, status=status.HTTP_403_FORBIDDEN)
    post.delete()
    
    return Response({"message":"post deleted successfully"},status=status.HTTP_200_OK)

@api_view(["GET"])
@jwt_required
def list_all_posts(request):
    post=Post.objects.all()
    serializer=PostSerializer(post,many=True)
    return Response({"posts":serializer.data},status=status.HTTP_200_OK)

@api_view(["GET"])
@jwt_required
def post_from_followeduser(request):
    following=Follow.objects.filter(follower=request.user)
    following_users=following.values_list('following')
    post=Post.objects.filter(user_id__in=following_users)
    if post:
        serializer = PostSerializer(post, many=True)
        return Response({"posts":serializer.data},status=status.HTTP_200_OK)
    return Response({"message":"no post"},status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
@jwt_required
def post_from_specificuser(request,user_id):
    post=Post.objects.filter(user_id=user_id)
    if post:
        serializer=PostSerializer(post,many=True)
        return Response({"posts":serializer.data},status=status.HTTP_200_OK)
    return Response({"message":"no post"},status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
@jwt_required
def retrieve_single_post(request,post_id):
    post=Post.objects.get(_id=post_id)
    serializer=PostSerializer(post)
    return Response({"post":serializer.data},status=status.HTTP_200_OK)

# @api_view(["POST"]) 
# @jwt_required 
# def like_post(request,post_id):
#     # likes=Like.object.filter(post_id=post_id,whose_post=)
#     like=Like.objects.get()
#     # user=User.objects.get() 
#     post=Post.objects.filter(_id=post_id)
#     data=request.data
#     like.post_id= data["post_id"]
#     like.whose_post= post.user_id
#     like.liked_by_whom= data["user_id"]
    
#     return Response({"messagae":"you liked"})



# create post 
# delete Post
# like post if already in database then delete else status like 
# want to see user profile
# want to see any post 
# do comment on any post you can do more then one comment 


