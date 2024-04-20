from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def register(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            messages.error(request,'Invalid Password')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exists...')
        else:
            user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
            user.save()
            profilepic=UserProfile(user=user)
            profilepic.save()
            login(request,user)
            return redirect('/')
    return render(request,'apptest/register.html')

def loggedin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Invalid Username or Password')
    return render(request,'apptest/login.html')

def loggedout(request):
    logout(request)
    return redirect('login')

def home(request):
    users=User.objects.exclude(username=request.user)
    context={'users':users}
    return render(request,'apptest/people.html',context)

def profile(request,pk):
    user=User.objects.get(id=pk)
    context={'user':user}
    return render(request,'apptest/profile.html',context)

def image(request,pk):
    image=Image.objects.get(id=pk)
    likes=PicLike.objects.filter(picpost=image).count()
    comments=ImageComment.objects.filter(image=image)
    form=ImageCommentForm()
    if request.method=='POST':
        form=ImageCommentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.image=image
            instance.hostname=request.user
            instance.save()
        return redirect('image',pk=pk)
    context={'image':image,'likes':likes,'form':form,'comments':comments}
    return render(request,'apptest/image.html',context)

def piclist(request):
    images=Image.objects.all()
    context={'images':images}
    return render(request,'apptest/piclist.html',context)

def videolist(request):
    videos=Video.objects.all()
    context={'videos':videos}
    return render(request,'apptest/video.html',context)

def photo(request,pk):
    user=User.objects.get(id=pk)
    images=Image.objects.filter(host=user)
    context={'images':images,'user':user}
    return render(request,'apptest/pic.html',context)

def piclike(request,post,user):
    user=User.objects.get(id=user)
    image=Image.objects.get(id=post)
    if PicLike.objects.filter(user=user,picpost=image).exists():
        like=PicLike.objects.get(user=user,picpost=image)
        like.delete()
        return redirect('image',pk=post)
    else:
        like=PicLike(user=user,picpost=image)
        like.save()
        return redirect('image',pk=post)

def addpic(request,pk):
    user=User.objects.get(id=pk)
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.host=request.user
            instance.save()
            return redirect('pic',pk=pk)
    else:
        form=ImageForm()
    context={'user':user,'form':form}
    return render(request,'apptest/addpic.html',context)

def video(request,pk):
    user=User.objects.get(id=pk)
    videos=Video.objects.filter(host=user)
    context={'user':user,'videos':videos}
    return render(request,'apptest/vid.html',context)

def addvid(request,pk):
    user=User.objects.get(id=pk)
    if request.method=='POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.host=request.user
            instance.save()
            return redirect('vid',pk=pk)
    else:
        form=VideoForm()
    context={'user':user,'form':form}
    return render(request,'apptest/addvid.html',context)


def vidcmt(request,pk):
    video=Video.objects.get(id=pk)
    likes=VidLike.objects.filter(vidpost=video).count()
    comments=VideoComment.objects.filter(video=video)
    form=VideoCommentForm()
    if request.method=='POST':
        form=VideoCommentForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.video=video
            instance.hostname=request.user
            instance.save()
        return redirect('vidcmt',pk=pk)
    context={'video':video,'likes':likes,'form':form,'comments':comments}
    return render(request,'apptest/vidcmt.html',context)

def vidlike(request,post,user):
    user=User.objects.get(id=user)
    video=Video.objects.get(id=post)
    if VidLike.objects.filter(user=user,vidpost=video).exists():
        like=VidLike.objects.get(user=user,vidpost=video)
        like.delete()
        return redirect('vidcmt',pk=post)
    else:
        like=VidLike(user=user,vidpost=video)
        like.save()
        return redirect('vidcmt',pk=post)

def delimage(request,pk):
    image=Image.objects.get(id=pk)
    id=image.host.id
    image.delete()
    return redirect('pic',pk=id)

def delvideo(request,pk):
    video=Video.objects.get(id=pk)
    id=video.host.id
    video.delete()
    return redirect('vid',pk=id)

def profileupdate(request,pk):
    user=User.objects.get(id=pk)
    profilepic=UserProfile.objects.get(user=user)
    userform=ProfileUpdateForm(instance=user)
    profileform=ProfilePicForm(instance=profilepic)
    if request.method=='POST':
        userform=ProfileUpdateForm(request.POST,instance=user)
        profileform=ProfilePicForm(request.POST,request.FILES,instance=profilepic)
        if userform.is_valid() and profileform.is_valid():
            custom=profileform.save(commit=False)
            custom.user=request.user
            userform.save()
            custom.save()
            return redirect('profile',pk=pk)
    context={'userform':userform,'profileform':profileform}
    return render(request,'apptest/profileupdate.html',context)

def save(request,post,user):
    user=User.objects.get(id=user)
    post=Image.objects.get(id=post)
    if SaveImage.objects.filter(user=user,image=post).exists():
        return redirect('image',pk=post.id)
    else:
        save=SaveImage(user=user,image=post)
        save.save()
        return redirect('image',pk=post.id)
    
def unsave(request,post,user):
    user=User.objects.get(id=user)
    post=Image.objects.get(id=post)
    unsave=SaveImage.objects.get(user=user,image=post)
    unsave.delete()
    return redirect('savelist',pk=user.id)

def saved(request,pk):
    user=User.objects.get(id=pk)
    savedlist=SaveImage.objects.filter(user=pk)
    vidsavedlist=SaveVideo.objects.filter(user=pk)
    context={'savedlist':savedlist,'user':user,'vidsavedlist':vidsavedlist}
    return render(request,'apptest/save.html',context)

def vidsave(request,post,user):
    user=User.objects.get(id=user)
    post=Video.objects.get(id=post)
    if SaveVideo.objects.filter(user=user,video=post).exists():
        return redirect('vidcmt',pk=post.id)
    else:
        save=SaveVideo(user=user,video=post)
        save.save()
        return redirect('vidcmt',pk=post.id)
    
def vidunsave(request,post,user):
    user=User.objects.get(id=user)
    post=Video.objects.get(id=post)
    unsave=SaveVideo.objects.get(user=user,video=post)
    unsave.delete()
    return redirect('savelist',pk=user.id)