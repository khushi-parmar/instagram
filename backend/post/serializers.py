from rest_framework_mongoengine.serializers import DocumentSerializer
from post.models import Post

class PostSerializer(DocumentSerializer):
    class Meta:
        model=Post
        fields=["_id","user_id","image","caption","created_at"]
        
    def create(self,validated_data):
        post=Post.objects.create(**validated_data)
        return post
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.image:
            rep['image'] = f"http://127.0.0.1:8000/api/v1/post/{instance._id}/image/"
        else:
            rep['image'] = None
        return rep 
    
