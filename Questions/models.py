from django.db import models
from django.contrib.auth.models import User 
from taggit.managers import TaggableManager



# Create your models here.


'''
Question :
    - user
    - title
    - content
    - created_at

Answer :
    - user
    - question
    - answer
    - created_at
'''

class Question(models.Model):
    user = models.ForeignKey(User,related_name='Question_user' , on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=30000)
    created_at = models.DateTimeField()
    tags = TaggableManager()


class Answer(models.Model):
    user = models.ForeignKey(User,related_name='Answer_user' , on_delete=models.SET_NULL,null=True)
    question = models.CharField(max_length=500)
    answer = models.TextField(max_length=30000)
    created_at = models.DateTimeField()
    tags = TaggableManager()
