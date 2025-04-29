from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Like 
from authentication.models import User

class LikeSerializer(DocumentSerializer):
    class Meta:
        model=Like
        fields=["post_id","liked_by_whom"]
    
    def create(self,validated_data):
        like=Like.objects.create(**validated_data)
        return like

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username']