from django.db import models
import re, time, datetime

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        today=str(datetime.date.today())
        print(today)
        # age = 
        emailRegex=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #determine login vs register with which key is in postdata
        if(postData['submission']=='Register'):
            if(len(postData['firstName'])<2 or len(postData['lastName'])<2):
                errors['name']='First and last name should be a least two characters'
            if(not postData['pw']==postData['cpw']):
                errors['pwMismatch']='Confirm Password does not match'
            if (time.strptime(postData['bDay'], '%Y-%m-%d')>time.strptime(today, '%Y-%m-%d')):
                errors['bDay']='Valid birthday needed'
            if (len(User.objects.filter(email=postData['email']))>0):
                errors['uniqueEmail']='this email has been registered!'
        if(not emailRegex.match(postData['email'])):
            errors['email']='Invalid email address!'
        if(len(postData['pw'])<8):
            errors['pwLen']='Password should be 8 characters long'
        return errors

class User(models.Model):
    firstName=models.CharField(max_length=55)
    lastName=models.CharField(max_length=55)
    email=models.CharField(max_length=55)
    pw=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    #posts=Post in wall.models