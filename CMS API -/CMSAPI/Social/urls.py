from django.urls import path, include
from Social.views import *

urlpatterns = [

    path("like" , Likes.as_view() ),
    path("likecounts" , Likecounts.as_view() ),
    path("" , user_opration.as_view() ),
    path("postinfo" , Post_blog_opration.as_view() ),
    path("content" , content.as_view() ),
    path("single" , postblogwithlike.as_view() ),

   
]
