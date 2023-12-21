from django.db import models
from django.contrib.auth.models import User

class PreRegistration(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    otp = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1,blank=False, null=False)

    def __str__(self):
        return f"PreRegistration for {self.user.username}"



class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class BlogContent(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=[('image', 'Image'), ('video', 'Video')])
    media_file = models.FileField(upload_to='blog_media/')  # Assuming you have a 'media' folder in your Django project

    def __str__(self):
        return f"{self.blog_post.title} - {self.content_type}"
