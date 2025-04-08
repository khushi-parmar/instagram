from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):  # Keep this as Serializer
    _id = serializers.CharField(read_only = True)  # Explicitly define ID
    username=serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=6)
    profile_pic = serializers.FileField(required=False, allow_null=True)
    created_at = serializers.DateTimeField(read_only=True)  # Explicitly define timestamps
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        profile_pic = validated_data.get('profile_pic')
        if profile_pic:
            # user.profile_pic.put(profile_pic, content_type=profile_pic.content_type)
            user.profile_pic = validated_data['profile_pic']
        user.set_password(validated_data['password'])  
        user.save()  
        return user 


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.profile_pic:
            rep['profile_pic'] = f"http://127.0.0.1:8000/api/v1/auth/user/{instance._id}/profile-pic/"
        else:
            rep['profile_pic'] = None
        return rep 
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


