from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
   #id는 django가 새로 만들어 줌
    name = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일 자동

class Room_Member(models.Model):
    room = models.ForeignKey(Room, to_field='id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

class Letter(models.Model):
    room = models.ForeignKey(Room, to_field='id', on_delete=models.CASCADE)
    author = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=10000)
    anniversary = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='letters/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
    letter = models.ForeignKey(Letter, to_field='id', on_delete=models.CASCADE)
    author = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)