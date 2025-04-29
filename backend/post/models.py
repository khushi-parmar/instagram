from django.db import models
from mongoengine import Document, StringField, EmailField, DateTimeField, ReferenceField,IntField
from datetime import datetime
import bcrypt
import uuid
from mongoengine.fields import FileField
from mongoengine import Document, ImageField
from authentication.models import User

# Create your models here.
class Post(Document):
    _id = StringField(default=lambda: str(uuid.uuid4()),primary_key = True)
    user_id=ReferenceField(User)
    image=ImageField(required=True)
    caption=StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    like_by_whom= ReferenceField(User,blank=True)
    

