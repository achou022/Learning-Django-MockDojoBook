from django.db import models
from login.models import User
import re, time, datetime

# Create your models here.
class contentManager(models.Manager):
    def validator(self, postData):
        errors={}
        # if(len(postData['post'])<10 or postData['post'].isspace()):
        #     errors['']='No SPAMS!'
        return errors

class Post(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=contentManager()
    #comments

class Comment(models.Model):
    content=models.TextField()
    user=models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=contentManager()