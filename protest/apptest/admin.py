from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Image,ImageComment,Video,VideoComment,UserProfile,PicLike,VidLike,SaveImage,SaveVideo])