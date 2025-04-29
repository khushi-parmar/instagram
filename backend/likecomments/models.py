from django.db import models
from mongoengine import StringField,ReferenceField,DateTimeField,Document
from datetime import datetime
import uuid
from post.models import Post
from authentication.models import User

# Create your models here.
class Like(Document):
    _id = StringField(default=lambda: str(uuid.uuid4()),primary_key = True)
    post_id=ReferenceField(Post)
    liked_by_whom=ReferenceField(User)
    created_at = DateTimeField(default=datetime.utcnow)
    status= StringField(default="liked")
