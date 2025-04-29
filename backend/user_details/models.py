from django.db import models
from mongoengine import Document,StringField,ReferenceField,DateTimeField
import uuid
from authentication.models import User
from datetime import datetime

# Create your models here.
class Follow(Document):
    _id = StringField(default=lambda: str(uuid.uuid4()),primary_key = True)
    follower=ReferenceField(User)
    status=StringField(default="followed")
    following=ReferenceField(User)
    created_at = DateTimeField(default=datetime.utcnow)
    
