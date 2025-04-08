from django.db import models

# Create your models here.
from mongoengine import Document, StringField, EmailField, DateTimeField
from datetime import datetime
import bcrypt
import uuid
from mongoengine.fields import FileField

from mongoengine import Document


class User(Document):
    _id = StringField(default=lambda: str(uuid.uuid4()),primary_key = True)
    username=StringField(required=True,unique=True,sparse=True)
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    profile_pic = FileField(blank=True, null=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    
    # Hash password before saving
    def set_password(self, raw_password):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Check password
    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))

