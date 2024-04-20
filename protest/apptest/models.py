from django.db import models
from django.contrib.auth.models import User
from datetime import *

# Create your models here.

class Image(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='pics')
    caption=models.CharField(max_length=50,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']

    def delete(self):
        self.image.delete()
        super().delete()

class PicLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    picpost=models.ForeignKey(Image,on_delete=models.CASCADE)

class ImageComment(models.Model):
    hostname=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000,blank=True,null=True)

class Video(models.Model):
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.FileField(upload_to='videos')
    caption=models.CharField(max_length=50,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created']

    def delete(self):
        self.video.delete()
        super().delete()

class VidLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    vidpost=models.ForeignKey(Video,on_delete=models.CASCADE)

class VideoComment(models.Model):
    hostname=models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.ForeignKey(Video,on_delete=models.CASCADE)
    comment=models.CharField(max_length=1000,blank=True,null=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic=models.ImageField(default='profile.png',upload_to='profilepics')

    def __str__(self):
        return self.user.username
    
class SaveImage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ForeignKey(Image,on_delete=models.CASCADE)

class SaveVideo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.ForeignKey(Video,on_delete=models.CASCADE)