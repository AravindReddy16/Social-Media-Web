from django import forms
from .models import *
from django.contrib.auth.models import User

class ImageCommentForm(forms.ModelForm):
    class Meta:
        model=ImageComment
        fields=['comment']

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['image','caption']

class VideoCommentForm(forms.ModelForm):
    class Meta:
        model=VideoComment
        fields=['comment']

class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['video','caption']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profilepic']