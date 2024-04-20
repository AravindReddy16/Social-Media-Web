from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('image/<str:pk>/',views.image,name='image'),
    path('register/',views.register,name='register'),
    path('login/',views.loggedin,name='login'),
    path('logout/',views.loggedout,name='logout'),
    path('',views.piclist,name='piclist'),
    path('pic/<str:pk>/',views.photo,name='pic'),
    path('addpic/<str:pk>/',views.addpic,name='addpic'),
    path('vid/<str:pk>/',views.video,name='vid'),
    path('addvid/<str:pk>/',views.addvid,name='addvid'),
    path('videos/',views.videolist,name='videolist'),
    path('video/<str:pk>/',views.vidcmt,name='vidcmt'),
    path('idelete/<str:pk>/',views.delimage,name='imagedelete'),
    path('vdelete/<str:pk>/',views.delvideo,name='videodelete'),
    path('update/<str:pk>/',views.profileupdate,name='profileupdate'),
    path('piclike/<str:post>/<str:user>/',views.piclike,name='piclike'),
    path('vidlike/<str:post>/<str:user>/',views.vidlike,name='vidlike'),
    path('savelist/<str:pk>/',views.saved,name='savelist'),
    path('save/<str:post>/<str:user>/',views.save,name='save'),
    path('vidsave/<str:post>/<str:user>/',views.vidsave,name='vidsave'),
    path('unsave/<str:post>/<str:user>/',views.unsave,name='unsave'),
    path('vidunsave/<str:post>/<str:user>/',views.vidunsave,name='vidunsave'),
]