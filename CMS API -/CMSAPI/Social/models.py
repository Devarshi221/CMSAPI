from django.db import models


class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=100)
    def __int__(self) :
        return self.user_id



class Post_blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(user, on_delete=models.CASCADE)                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    is_public = models.BooleanField(default=True)
    def __str__(self) :
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post_blog, on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    