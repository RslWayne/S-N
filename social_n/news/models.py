from datetime import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class News(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=300)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering =['-created_date']

    #like_set
    #dislike_set


class Image(models.Model):
    image = models.ImageField()
    news = models.ForeignKey(News,on_delete=models.CASCADE,null=True)


class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=250)



class Like(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Dislike(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Profile(models.Model):
    gender = (
        ('F', 'F'),
        ('M', 'M')
 )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200,blank=True)
    age = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    gender = models.CharField(choices=gender,max_length=20)
    email = models.CharField(max_length=100)
    github = models.CharField(max_length=250)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    desc = models.TextField()
    hobbies = models.TextField()
    friends =models.ManyToManyField(User,blank=True,related_name='friends')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(default='avatar.png',upload_to='avatars/')



class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField()
    comments = models.TextField()


